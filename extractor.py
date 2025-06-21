import os
import json
import time
import os
import google.generativeai as genai

try:
    # Try to import streamlit for cloud deployment
    import streamlit as st
    # Use Streamlit secrets in cloud environment
    api_key = st.secrets["GOOGLE_API_KEY"]
except ImportError:
    # Fallback to dotenv for local development
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("Google API key not found in environment variables or Streamlit secrets")
genai.configure(api_key=api_key)

def generate_content_with_retry(uploaded_file, prompt, max_retries=3):
    """Generate content with retry logic and exponential backoff"""
    base_delay = 1  # Start with 1 second delay
    
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1} of {max_retries}")
            
            # Initialize the Gemini model
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            response = model.generate_content([
                uploaded_file,
                prompt
            ])
            
            if response and response.text:
                response_text = response.text.strip()
                
                # Clean up response if it contains markdown formatting
                if response_text.startswith('```json'):
                    response_text = response_text.strip('```json\n').strip('```').strip()
                elif response_text.startswith('```'):
                    response_text = response_text.strip('```').strip()
                
                return response_text
            else:
                print("API response did not contain valid text.")
                
        except Exception as api_error:
            print(f"API call attempt {attempt + 1} failed: {api_error}")
            
            # Check if this is the last attempt
            if attempt == max_retries - 1:
                error_details = str(api_error)
                if "RESOURCE_EXHAUSTED" in error_details or "quota" in error_details.lower():
                    print("API quota exhausted. Please try again later.")
                elif "PERMISSION_DENIED" in error_details:
                    print("API permission denied. Please check your API key.")
                elif "INVALID_ARGUMENT" in error_details:
                    print("Invalid request format. Document might be too large.")
                return None
            
            # Wait before retrying (exponential backoff)
            delay = base_delay * (2 ** attempt)
            print(f"Waiting {delay} seconds before retry...")
            time.sleep(delay)
    
    return None

def process_single_file(file_path):
    """Process a single PDF file and extract data"""
    uploaded_file = None
    try:
        # Upload file to Gemini
        uploaded_file = genai.upload_file(file_path)
        
        # Wait for file to be processed
        while uploaded_file.state.name == "PROCESSING":
            print(f"Processing file: {uploaded_file.name}")
            time.sleep(2)
            uploaded_file = genai.get_file(uploaded_file.name)
        
        if uploaded_file.state.name == "FAILED":
            print(f"File processing failed: {uploaded_file.name}")
            return []

        
        # Construct the prompt
        prompt = """
        You are an expert at extracting data from Certificate of Analysis (CoA) documents.
        
        Please extract the following information from this PDF and return it as a JSON array:
        
        For each batch/lot found in the document, create an object with:
        {
            "batch_number": "the batch/lot number",
            "analytical_parameters": [
                {
                    "parameter": "parameter name with units if available",
                    "result": "the test result/value",
                    "method": "analysis method if mentioned"
                }
            ]
        }
        
        Important guidelines:
        - Look for batch numbers, lot numbers, or similar identifiers
        - Extract all analytical parameters (tests performed)
        - Include units with parameter names when available
        - Capture the actual test results/values
        - Include analysis methods and reference methods when mentioned
        - Return only valid JSON, no additional text
        - If no data is found, return an empty array []
        """
        
        # Generate content with retry logic
        response = generate_content_with_retry(uploaded_file, prompt)
        
        if response:
            try:
                # Parse JSON response
                extracted_data = json.loads(response)
                return extracted_data if isinstance(extracted_data, list) else []
            except json.JSONDecodeError as e:
                print(f"JSON parsing error: {e}")
                print(f"Raw response: {response[:500]}...")  # Limit output length
                return []
        
        return []
        
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return []
    finally:
        # Clean up uploaded file from Gemini
        if uploaded_file:
            try:
                genai.delete_file(uploaded_file.name)
            except Exception as e:
                print(f"Warning: Could not delete uploaded file {uploaded_file.name}: {e}")
