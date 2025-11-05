# PDF to Text Converter - Usage Guide

## Quick Start

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/MEKALA-JASWANTH/PDF_to_Text_Converter.git
   cd PDF_to_Text_Converter
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python pdf_converter.py
   ```

---

## Main Features - Step by Step

### 1. Launch Application
- Run `python pdf_converter.py`
- A Tkinter window will open with the PDF to Text Converter interface
- The window is 900x700 pixels with a professional dark theme

### 2. Select PDF Files

**How to Select Files:**
1. Click the **"Select PDF File(s)"** button (Blue color)
2. A file browser dialog opens
3. Browse to your PDF files location
4. Select one or multiple PDF files
5. Click **"Open"** to confirm
6. Selected filenames appear in the "Selected Files" list
7. You'll see a confirmation message showing how many files were selected

**Tips:**
- Select multiple files using Ctrl+Click (Windows/Linux) or Cmd+Click (Mac)
- Use Shift+Click to select a range of files
- Only PDF files are supported

### 3. Extract Text

**How to Extract Text:**
1. Click the **"Extract Text"** button (Green color)
2. Application processes all selected PDF files
3. Text content appears in the "Extracted Text" display area
4. Status bar shows completion message with page count
5. Success message appears when extraction is complete

**What Happens During Extraction:**
- Each file is opened and processed
- Text is extracted from each page
- Pages are clearly marked in the output
- Multiple files are combined with file headers separating them
- Page information is included (e.g., "--- Page 1 ---")

**Error Handling:**
- If a file is corrupted or cannot be read, an error message appears
- Extraction stops and displays the specific error
- You can try with different files or check file integrity

### 4. Save Extracted Text

**How to Save Text:**
1. Click the **"Save as TXT"** button (Orange color)
2. A save dialog opens
3. Choose where to save the file
4. Default filename is `extracted_text_YYYYMMDD_HHMMSS.txt`
5. You can modify the filename
6. Click **"Save"** to save
7. Confirmation message appears

**File Details:**
- Files are saved as UTF-8 text files
- Timestamps in filename prevent file overwrites
- You can save multiple extractions
- File includes all page markers and separators

### 5. Clear Display

**How to Clear:**
1. Click the **"Clear Display"** button (Red color)
2. All extracted text is removed from display
3. File list is cleared
4. Application resets to ready state
5. Confirmation message appears

**When to Clear:**
- Before processing a new batch of PDFs
- To free up memory for large documents
- To start fresh

---

## Understanding the Interface

### Header Section
- **Title**: "PDF to Text Converter" - identifies the application
- **Dark Blue Background**: Professional appearance

### Button Panel
- **Select PDF File(s)** (Blue): Browse and select PDFs
- **Extract Text** (Green): Extract text from selected PDFs
- **Save as TXT** (Orange): Export extracted text
- **Clear Display** (Red): Reset application

### Status Bar
- Shows current operation status
- Displays file counts and statistics
- Updates in real-time

### Selected Files List
- Shows filenames of selected PDFs
- Scrollable for many files
- Updated after selection

### Extracted Text Display
- Large text area showing content
- Supports scrolling
- Read-only (non-editable)
- Displays with monospace font for clarity

### Footer Section
- **Credit Line**: "Created by Jaswanth | Advanced Python Project"
- Application identifier

---

## Workflow Examples

### Example 1: Single File Extraction
```
1. Start application
2. Click "Select PDF File(s)"
3. Choose: report.pdf
4. Click "Extract Text"
5. Review extracted text
6. Click "Save as TXT"
7. Save as: report_text.txt
```

### Example 2: Batch Processing Multiple Files
```
1. Start application
2. Click "Select PDF File(s)"
3. Select: document1.pdf, document2.pdf, document3.pdf
4. Click "Extract Text"
5. All three files are processed and combined
6. Review complete extracted text
7. Save as single text file with all content
```

### Example 3: Processing and Re-extraction
```
1. Extract text from PDF
2. Save as output.txt
3. Click "Clear Display"
4. Select different PDFs
5. Extract again
6. Save with new filename
```

---

## Keyboard Shortcuts (Advanced)

If using a Python IDE or terminal:
- **Ctrl+C**: Stop application from terminal
- **Alt+F4**: Close application window
- **Ctrl+A**: Select all text in display (if editable)

---

## Tips and Tricks

### For Better Results
1. **Use Clear PDFs**: Text-based PDFs work best
2. **Check File Size**: Keep PDFs under 100 MB
3. **One Format Per Batch**: Process similar PDFs together
4. **Save Regularly**: Don't process too many files at once
5. **Organize Output**: Use descriptive filenames

### Performance Tips
1. Close other applications for faster processing
2. Use an SSD for better file I/O performance
3. Process files in batches rather than all at once
4. Clear display between batches to free memory

### Troubleshooting

**Problem: "No module named 'PyPDF2'"**
- Solution: Run `pip install PyPDF2`

**Problem: "No PDFs extracted"**
- Solution: Make sure to click "Extract Text" button
- Check that PDF files are not password-protected

**Problem: Application window doesn't appear**
- Solution: Ensure Python and Tkinter are properly installed
- Run from command line to see any errors

**Problem: "Permission denied" when saving**
- Solution: Choose a different folder (Documents, Downloads)
- Check folder permissions
- Run application as administrator if needed

**Problem: Extracted text is incomplete**
- Solution: PDF might be scanned image (needs OCR)
- Try with different PDF file
- Check PDF integrity

---

## Advanced Usage

### Configuration
The `config.py` file contains all customizable settings:
- Window size and colors
- Font configurations
- File handling options
- Text processing settings

### Utilities
The `utils.py` file provides helper functions:
- File validation
- Text processing
- PDF information extraction
- Logging capabilities

### Integration
You can import the converter class in your own scripts:
```python
from pdf_converter import PDFToTextConverter
import tkinter as tk

root = tk.Tk()
app = PDFToTextConverter(root)
root.mainloop()
```

---

## Output Format

### Text Structure
```
================================================================================
File: document.pdf
Pages: 5
================================================================================

--- Page 1 ---
[Page 1 content here]

--- Page 2 ---
[Page 2 content here]

...
```

### Save Location
- Default: Same folder where you run the application
- Custom: Choose any accessible location
- Format: UTF-8 encoded plain text

---

## Frequently Asked Questions

**Q: Can I edit extracted text in the application?**
A: No, the text display is read-only. Copy text and edit in a text editor.

**Q: What file formats are supported?**
A: Only PDF files (.pdf). Other formats are not supported.

**Q: Can I process scanned PDFs?**
A: No, scanned PDFs require OCR which is not included. Only text-based PDFs work.

**Q: How large can PDF files be?**
A: Theoretically unlimited, but performance decreases with size. Tested up to 100 MB.

**Q: Can I process password-protected PDFs?**
A: No, password-protected PDFs are not supported in this version.

**Q: Is there a limit to how many files I can process?**
A: No hard limit, but processing time increases with file count.

---

## Support and Contributions

For issues, suggestions, or contributions:
- Visit: https://github.com/MEKALA-JASWANTH/PDF_to_Text_Converter
- Create an issue for bug reports
- Submit pull requests for improvements

---

## Version Information
- **Version**: 1.0.0
- **Status**: Production Ready
- **Created by**: Jaswanth
- **Last Updated**: November 2025

---

**Happy converting!**
