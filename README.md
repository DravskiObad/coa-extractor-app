# CoA Extraction App 📊

An AI-powered web application that automatically extracts analytical data from Certificate of Analysis (CoA) PDF documents using Google's Gemini AI model.

## 🌟 Features

- **AI-Powered Extraction**: Automatically identifies and extracts:
  - Batch/lot numbers
  - Analytical parameters with units
  - Test results and values
  - Analysis methods
- **Multi-file Processing**: Upload and process multiple PDF files simultaneously
- **Smart Data Restructuring**: Organizes extracted data into standardized tables
- **Export Functionality**: Download results as professionally formatted Word documents
- **User-Friendly Interface**: Modern, responsive design with real-time progress tracking
- **Session Management**: Maintains state across user interactions

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **Backend**: Python
- **Document Processing**: python-docx
- **Data Handling**: pandas

## 📖 Usage

1. **Upload PDF Files**: Select one or more CoA PDF documents (max 10 pages each)
2. **Extract Data**: Click the "Extract Data" button to process files
3. **Review Results**: View extracted data in a structured table format
4. **Export**: Download results as a Word document for further use
5. **Clear Data**: Use the clear button to reset and start a new extraction

## ⚠️ Important Notes

- **File Size**: Split large CoAs into smaller files (max 10 pages)
- **Confidentiality**: Only upload non-confidential versions of documents
- **Supported Formats**: PDF files only
- **Processing Time**: Varies based on document complexity and API response time

### Streamlit Configuration

The app uses the following Streamlit configuration:
- Wide layout for better data visualization
- Collapsed sidebar for cleaner interface
- Custom CSS styling for professional appearance

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google AI**: For providing the Gemini AI model
- **Streamlit**: For the excellent web app framework
- **European Food Safety Authority**: For project inspiration and support

## 📊 Example Output

The application extracts data and presents it in a structured format:

| Parameter (unit) | Batch 001 | Batch 002 | Method of analysis |
|------------------|-----------|-----------|--------------------|
| Moisture (%) | 5.2 | 4.8 | AOAC 925.10 |
| Protein (%) | 12.5 | 12.8 | Kjeldahl method |
| pH | 6.8 | 6.9 | Potentiometry |

---

**Powered by Google Gemini 2.5 Flash 2025**
