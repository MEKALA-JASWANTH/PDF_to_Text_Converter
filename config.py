"""
Configuration Module for PDF to Text Converter
Contains all customizable settings and constants
Created by Jaswanth
"""

# ============================================================================
# APPLICATION CONFIGURATION
# ============================================================================

# Window Configuration
WINDOW_TITLE = "PDF to Text Converter"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 600

# ============================================================================
# COLOR SCHEME (Modern Dark Theme)
# ============================================================================

COLORS = {
    'primary_dark': '#2c3e50',      # Header background
    'primary_light': '#34495e',     # Footer background
    'button_primary': '#3498db',    # Select files button
    'button_success': '#27ae60',    # Extract text button
    'button_warning': '#f39c12',    # Save button
    'button_danger': '#e74c3c',     # Clear button
    'background': '#f0f0f0',        # Main background
    'text_light': '#ecf0f1',        # Light text areas
    'text_dark': '#2c3e50',         # Dark text
    'text_white': '#ffffff',        # White text
}

# ============================================================================
# FONT CONFIGURATION
# ============================================================================

FONTS = {
    'title': ('Arial', 20, 'bold'),
    'heading': ('Arial', 10, 'bold'),
    'normal': ('Arial', 9),
    'button': ('Arial', 10, 'bold'),
    'mono': ('Courier', 9),  # For text display
}

# ============================================================================
# FILE HANDLING CONFIGURATION
# ============================================================================

# PDF File Settings
PDF_FILETYPES = [("PDF Files", "*.pdf"), ("All Files", "*.*")]

# Text File Settings
TXT_FILETYPES = [("Text Files", "*.txt"), ("All Files", "*.*")]
TEXT_ENCODING = 'utf-8'

# File Naming Convention
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
DEFAULT_OUTPUT_PREFIX = "extracted_text"
DEFAULT_OUTPUT_EXTENSION = ".txt"

# ============================================================================
# TEXT EXTRACTION CONFIGURATION
# ============================================================================

# Page Header/Footer Configuration
PAGE_SEPARATOR = "="*80
PAGE_MARKER_FORMAT = "--- Page {page_num} ---"
FILE_HEADER_FORMAT = "File: {filename}\nPages: {num_pages}"

# Text Processing
ADD_PAGE_NUMBERS = True
ADD_FILE_HEADERS = True
PRESERVE_WHITESPACE = True

# ============================================================================
# UI MESSAGE CONFIGURATION
# ============================================================================

MESSAGES = {
    'title': 'PDF to Text Converter',
    'select_files': 'Select PDF File(s)',
    'extract_text': 'Extract Text',
    'save_text': 'Save as TXT',
    'clear_display': 'Clear Display',
    'status_ready': 'Ready',
    'status_files_selected': '{count} file(s) selected',
    'status_extraction_success': 'Successfully extracted text from {count} file(s) ({pages} pages total)',
    'status_save_success': 'Text saved successfully to {filename}',
    'status_cleared': 'Display cleared',
    'error_no_files': 'Please select at least one PDF file first!',
    'error_no_text': 'No extracted text to save. Please extract text first!',
    'error_extraction': 'Error extracting text: {error}',
    'error_save': 'Error saving file: {error}',
    'success_selection': 'Selected {count} PDF file(s)',
    'success_extraction': 'Successfully extracted text from {count} file(s) ({pages} pages total)',
    'success_save': 'Text saved successfully to {filename}',
    'success_clear': 'Display cleared and ready for new extraction',
}

# ============================================================================
# LABEL CONFIGURATION
# ============================================================================

LABELS = {
    'selected_files': 'Selected Files:',
    'extracted_text': 'Extracted Text:',
    'status': 'Status:',
    'footer': 'Created by Jaswanth | Advanced Python Project',
}

# ============================================================================
# BUTTON PADDING CONFIGURATION
# ============================================================================

BUTTON_PADDING = {
    'padx': 15,
    'pady': 8,
}

# ============================================================================
# LISTBOX CONFIGURATION
# ============================================================================

FILE_LISTBOX_HEIGHT = 4

# ============================================================================
# TEXT DISPLAY CONFIGURATION
# ============================================================================

TEXT_DISPLAY_HEIGHT = 15
TEXT_DISPLAY_WRAP = 'word'

# ============================================================================
# FEATURES
# ============================================================================

FEATURES = {
    'multi_file_selection': True,
    'drag_and_drop': False,  # Future enhancement
    'batch_processing': True,
    'export_single_file': True,
    'auto_timestamp': True,
    'error_recovery': True,
    'status_notifications': True,
}

# ============================================================================
# VALIDATION SETTINGS
# ============================================================================

VALIDATION = {
    'require_file_selection': True,
    'max_file_size_mb': 100,  # Max PDF file size
    'supported_extensions': ['.pdf'],
}

# ============================================================================
# PERFORMANCE SETTINGS
# ============================================================================

PERFORMANCE = {
    'buffer_size': 1024,
    'update_interval_ms': 100,
}
