# CoA Extraction App - Streamlit Version

This is a Streamlit version of the Certificate of Analysis (CoA) extraction application that uses Google Gemini AI to extract structured data from PDF documents.

## Features

- 📄 Upload multiple PDF files containing Certificates of Analysis
- 🤖 AI-powered extraction using Google Gemini API
- 📊 Structured data display in table format
- 💾 Export results to Word documents
- 🌐 Web-based interface accessible from any browser

## Local Development

### Prerequisites

- Python 3.8 or higher
- Google API key for Gemini API

### Installation

1. Install dependencies:
```bash
pip install -r requirements_streamlit.txt
```

2. Create a `.env` file with your Google API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```

3. Run the application:
```bash
streamlit run streamlit_app.py
```

## Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Create a new GitHub repository
2. Upload these files to your repository:
   - `streamlit_app.py` (main application)
   - `extractor.py` (AI processing logic)
   - `requirements_streamlit.txt` (dependencies)
   - `.env` (your environment variables)

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set the main file path to: `streamlit_app.py`
6. Click "Deploy!"

### Step 3: Configure Environment Variables

1. In your Streamlit Cloud app settings, go to "Secrets"
2. Add your environment variables:
```toml
GOOGLE_API_KEY = "your_google_api_key_here"
```

### Important Notes

- **File Size Limits**: Keep PDF files under 10 pages for best performance
- **API Limits**: Google Gemini API has usage quotas - monitor your usage
- **Security**: Never commit your `.env` file with real API keys to public repositories
- **Performance**: Processing time depends on file size and API response time

## File Structure

```
CoA extractor app v2/
├── streamlit_app.py          # Main Streamlit application
├── extractor.py              # AI processing logic
├── requirements_streamlit.txt # Python dependencies
├── .env                      # Environment variables (local only)
└── README_Streamlit.md       # This file
```

## Usage Instructions

1. **Upload Files**: Use the file uploader to select PDF files
2. **Extract Data**: Click the "Extract Data" button to process files
3. **Review Results**: View the extracted data in the table format
4. **Download**: Export results as a Word document
5. **Clear Data**: Use the clear button to start a new session

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Google API key is correctly set in environment variables
2. **File Processing Failed**: Check if PDF files are readable and under size limits
3. **No Data Extracted**: Verify that PDFs contain Certificate of Analysis data
4. **Slow Processing**: Large files or high API usage may cause delays

### Getting Help

- Check the Streamlit Cloud logs for detailed error messages
- Verify your Google API key has Gemini API access enabled
- Ensure all dependencies are correctly listed in requirements_streamlit.txt

## Differences from Flask Version

- **No Session Management**: Streamlit handles state management automatically
- **Simplified UI**: Streamlit provides built-in components for file upload and display
- **Real-time Updates**: Progress bars and status updates during processing
- **Responsive Design**: Automatically adapts to different screen sizes
- **Easy Deployment**: One-click deployment to Streamlit Cloud

## Security Considerations

- API keys are stored securely in Streamlit Cloud secrets
- Uploaded files are processed temporarily and not stored permanently
- All processing happens server-side for security

---

**Powered by European Food Safety Authority 2025**