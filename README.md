# PDF to Text Converter

## Overview
An advanced-level Python project featuring a professional Tkinter GUI application that converts PDF files to plain text format. This project demonstrates object-oriented programming, file handling, GUI development, and user experience design without using machine learning or complex algorithms.

**Created by:** Jaswanth  
**Project Type:** Advanced Python | GUI Application  
**License:** MIT

---

## Features Added by Jaswanth

### 1. **Tkinter GUI Interface**
   - Professional, user-friendly graphical interface
   - Modern color scheme (#2c3e50, #3498db, #27ae60)
   - Organized layout with header, content area, and footer
   - Responsive design that adapts to window resizing

### 2. **PDF File Selection**
   - Multi-file selection capability
   - Browse and select one or multiple PDF files
   - File list display with scrollbar for easy navigation
   - Shows selected filenames before processing

### 3. **Text Extraction Engine**
   - Utilizes PyPDF2 library for robust PDF text extraction
   - Extracts text from all pages in selected PDFs
   - Handles multiple PDF files in a single operation
   - Organizes extracted text with file headers and page markers
   - Displays page numbers for reference
   - Error handling for corrupted or protected PDFs

### 4. **Display and Preview**
   - ScrolledText widget for viewing extracted content
   - Real-time display of extracted text
   - Support for large documents with automatic scrolling
   - Text appears with proper formatting and page separation

### 5. **Save Functionality**
   - Export extracted text to .txt files
   - Automatic filename generation with timestamps (YYYY-MM-DD_HHMMSS)
   - UTF-8 encoding for international character support
   - Custom save location selection via file dialog
   - Preserves formatting with page markers and file headers

### 6. **Export All to Single File**
   - Combines text from multiple PDFs into one text file
   - Clear separation between different source files
   - Page information included for each document
   - Chronological organization of content

### 7. **Clear Display Function**
   - Reset all data and UI elements
   - Clear extracted text from display
   - Reset file list
   - Clean state ready for new extraction
   - Confirmation via message box

### 8. **User Notifications**
   - Success messages after file selection
   - Status bar showing real-time operation status
   - Error messages with detailed descriptions
   - Confirmation dialogs for important actions
   - Message boxes for user feedback
   - Page count and file statistics display

### 9. **Status Tracking**
   - Dynamic status label showing current operation
   - File count information
   - Page count statistics
   - Clear indication of success or failure
   - Helpful prompts for user actions

### 10. **Error Handling**
   - Try-catch blocks for robust error management
   - Validation before processing
   - File access error handling
   - PDF parsing error handling
   - File write error handling
   - User-friendly error messages

---

## Technical Implementation

### Architecture
```
PDFToTextConverter (Main Class)
├── __init__()           - Initialize application
├── setup_ui()           - Create GUI components
├── select_files()       - Handle file selection
├── extract_text()       - Extract text from PDFs
├── save_text()          - Save extracted text
├── clear_display()      - Reset application
└── update_status()      - Update status messages
```

### Libraries Used
- **Tkinter**: Built-in GUI framework (no installation needed)
- **PyPDF2**: PDF parsing and text extraction
- **os**: File path operations
- **datetime**: Timestamp generation

### Code Quality
- Object-oriented design patterns
- Docstrings for all methods
- Clear variable naming conventions
- Proper exception handling
- Clean code organization

---

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/MEKALA-JASWANTH/PDF_to_Text_Converter.git
   cd PDF_to_Text_Converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python pdf_converter.py
   ```

---

## Usage Guide

### Step-by-Step Instructions

#### 1. **Select PDF Files**
   - Click the "Select PDF File(s)" button
   - Browse to your PDF documents
   - Select one or multiple PDF files
   - Click "Open" to confirm
   - Selected files appear in the file list

#### 2. **Extract Text**
   - Click the "Extract Text" button
   - Application processes all selected PDFs
   - Extracted text appears in the display area
   - Status bar shows completion and page count

#### 3. **Save Text**
   - Click the "Save as TXT" button
   - Choose save location and filename
   - File saves with UTF-8 encoding
   - Confirmation message appears

#### 4. **Clear Display**
   - Click the "Clear Display" button to reset
   - All data, text, and file list are cleared
   - Application ready for new extraction

### Example Workflow
```
1. Start application → pdf_converter.py
2. Select files → Choose PDF documents
3. Extract text → Process selected PDFs
4. Save result → Export to .txt file
5. Clear → Reset for next batch
```

---

## GUI Components

### Header Section
- **Title Bar**: "PDF to Text Converter" (Dark theme)
- **Background Color**: #2c3e50 (Professional dark blue)

### Button Panel
- **Select PDF File(s)**: Blue (#3498db) - File selection
- **Extract Text**: Green (#27ae60) - Text extraction
- **Save as TXT**: Orange (#f39c12) - File export
- **Clear Display**: Red (#e74c3c) - Reset application

### Display Areas
- **Status Label**: Shows current operation status
- **File List**: Displays selected PDF filenames
- **Text Display**: Shows extracted text content

### Footer Section
- **Credit**: "Created by Jaswanth | Advanced Python Project"
- **Background Color**: #34495e (Darker theme)

---

## File Structure
```
PDF_to_Text_Converter/
├── README.md              # This file
├── requirements.txt       # Project dependencies
├── pdf_converter.py       # Main application
└── .gitignore            # Git ignore file
```

---

## Performance Characteristics

- **Startup Time**: < 1 second
- **PDF Processing**: Depends on file size and page count
- **Memory Usage**: Efficient for files up to several hundred pages
- **GUI Responsiveness**: Smooth and interactive

---

## Limitations & Future Enhancements

### Current Limitations
- Password-protected PDFs not supported (would require additional library)
- Scanned PDFs with images cannot be converted (would require OCR)
- Complex layouts may lose formatting

### Potential Enhancements
- Add OCR support for scanned PDFs
- Implement batch processing with progress bar
- Add text search and highlight functionality
- Support for password-protected PDFs
- Export to multiple formats (DOCX, PDF, RTF)
- Dark/Light theme toggle
- Recent files history
- Drag-and-drop file support

---

## Troubleshooting

### Issue: "No module named 'PyPDF2'"
**Solution**: Install PyPDF2 using `pip install PyPDF2`

### Issue: "No PDFs extracted"
**Solution**: Ensure you've selected PDF files and clicked "Extract Text" button

### Issue: "Permission denied when saving"
**Solution**: Check file permissions and choose a different save location

### Issue: "Application window doesn't open"
**Solution**: Ensure Tkinter is installed (usually built-in with Python)

---

## Project Highlights

✅ **Advanced Python Concepts**
- Object-oriented programming (OOP)
- GUI development with Tkinter
- File I/O operations
- Exception handling
- List and data structure management

✅ **Professional Features**
- Intuitive user interface
- Robust error handling
- User feedback system
- Clean code architecture
- Comprehensive documentation

✅ **No External Complexity**
- No machine learning
- No complex algorithms
- No external dependencies beyond PyPDF2
- Pure Python implementation

---

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.

## License
This project is licensed under the MIT License - feel free to use it in your own projects.

## Author
**Jaswanth**
- GitHub: [@MEKALA-JASWANTH](https://github.com/MEKALA-JASWANTH)

---

## Acknowledgments
- PyPDF2 library for PDF processing
- Python Tkinter community for GUI resources
- Advanced Python programming best practices

**Last Updated**: November 2025  
**Version**: 1.0.0  
**Status**: Production Ready
