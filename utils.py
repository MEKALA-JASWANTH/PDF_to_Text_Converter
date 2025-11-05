"""
Utility Functions Module for PDF to Text Converter
Provides helper functions for the application
Created by Jaswanth
"""

import os
from datetime import datetime
from pathlib import Path


class FileUtilities:
    """Utility class for file operations."""
    
    @staticmethod
    def get_filename_without_extension(filepath):
        """Get filename without extension."""
        return os.path.splitext(os.path.basename(filepath))[0]
    
    @staticmethod
    def get_file_size(filepath):
        """Get file size in MB."""
        try:
            size_bytes = os.path.getsize(filepath)
            return size_bytes / (1024 * 1024)  # Convert to MB
        except Exception:
            return 0
    
    @staticmethod
    def get_file_extension(filepath):
        """Get file extension."""
        return os.path.splitext(filepath)[1].lower()
    
    @staticmethod
    def is_valid_pdf(filepath):
        """Check if file is a valid PDF."""
        return FileUtilities.get_file_extension(filepath) == '.pdf'
    
    @staticmethod
    def create_backup_filename(filename):
        """Create a backup filename with timestamp."""
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{name}_backup_{timestamp}{ext}"
    
    @staticmethod
    def ensure_directory_exists(directory):
        """Ensure directory exists, create if not."""
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def get_total_files_size(file_list):
        """Calculate total size of all files."""
        return sum(FileUtilities.get_file_size(f) for f in file_list)


class TextUtilities:
    """Utility class for text operations."""
    
    @staticmethod
    def truncate_text(text, max_length=100, suffix="..."):
        """Truncate text to maximum length."""
        if len(text) > max_length:
            return text[:max_length] + suffix
        return text
    
    @staticmethod
    def count_words(text):
        """Count words in text."""
        return len(text.split())
    
    @staticmethod
    def count_lines(text):
        """Count lines in text."""
        return len(text.split('\n'))
    
    @staticmethod
    def get_text_statistics(text):
        """Get comprehensive text statistics."""
        stats = {
            'characters': len(text),
            'words': TextUtilities.count_words(text),
            'lines': TextUtilities.count_lines(text),
            'paragraphs': len([p for p in text.split('\n\n') if p.strip()]),
        }
        return stats
    
    @staticmethod
    def remove_extra_whitespace(text):
        """Remove extra whitespace from text."""
        return ' '.join(text.split())
    
    @staticmethod
    def normalize_line_endings(text):
        """Normalize line endings to LF."""
        return text.replace('\r\n', '\n').replace('\r', '\n')


class PDFUtilities:
    """Utility class for PDF operations."""
    
    @staticmethod
    def validate_pdf_file(filepath):
        """Validate if file exists and is a PDF."""
        if not os.path.exists(filepath):
            return False, "File not found"
        
        if not FileUtilities.is_valid_pdf(filepath):
            return False, "File is not a PDF"
        
        if os.path.getsize(filepath) == 0:
            return False, "PDF file is empty"
        
        return True, "Valid PDF file"
    
    @staticmethod
    def get_pdf_info(filepath):
        """Get PDF file information."""
        return {
            'filename': os.path.basename(filepath),
            'size_mb': FileUtilities.get_file_size(filepath),
            'created': datetime.fromtimestamp(os.path.getctime(filepath)),
            'modified': datetime.fromtimestamp(os.path.getmtime(filepath)),
        }


class DateTimeUtilities:
    """Utility class for date and time operations."""
    
    @staticmethod
    def get_current_timestamp():
        """Get current timestamp in standard format."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def get_filename_timestamp():
        """Get timestamp suitable for filenames."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def format_datetime(dt, format_string="%Y-%m-%d %H:%M:%S"):
        """Format datetime object."""
        return dt.strftime(format_string)


class ValidationUtilities:
    """Utility class for validation operations."""
    
    @staticmethod
    def validate_file_list(files):
        """Validate list of files."""
        if not files:
            return False, "No files selected"
        
        valid_files = []
        for file in files:
            is_valid, msg = PDFUtilities.validate_pdf_file(file)
            if is_valid:
                valid_files.append(file)
        
        if not valid_files:
            return False, "No valid PDF files found"
        
        return True, f"{len(valid_files)} valid file(s)"
    
    @staticmethod
    def validate_save_path(path):
        """Validate save path."""
        directory = os.path.dirname(path)
        
        if directory and not os.path.exists(directory):
            return False, "Directory does not exist"
        
        if os.path.exists(path):
            return True, "File will be overwritten"
        
        return True, "Valid save path"


class LogUtilities:
    """Utility class for logging operations."""
    
    @staticmethod
    def create_log_entry(action, status, details=""):
        """Create a log entry."""
        timestamp = DateTimeUtilities.get_current_timestamp()
        return f"[{timestamp}] {action}: {status} {details}"
    
    @staticmethod
    def log_to_file(filename, entry):
        """Log entry to file."""
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(entry + '\n')
            return True
        except Exception:
            return False
