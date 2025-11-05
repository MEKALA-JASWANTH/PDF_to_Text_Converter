import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import PyPDF2
import os
from datetime import datetime

class PDFToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to Text Converter")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        self.selected_files = []
        self.extracted_text = ""
        
        self.setup_ui()
    
    def setup_ui(self):
        """Create the user interface."""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title_label = tk.Label(header_frame, text="PDF to Text Converter", 
                              font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
        title_label.pack(pady=15)
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg="#f0f0f0")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button frame
        button_frame = tk.Frame(content_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, pady=10)
        
        # Select files button
        self.select_btn = tk.Button(button_frame, text="Select PDF File(s)", 
                                   command=self.select_files,
                                   bg="#3498db", fg="white", padx=15, pady=8,
                                   font=("Arial", 10, "bold"))
        self.select_btn.pack(side=tk.LEFT, padx=5)
        
        # Extract text button
        self.extract_btn = tk.Button(button_frame, text="Extract Text", 
                                    command=self.extract_text,
                                    bg="#27ae60", fg="white", padx=15, pady=8,
                                    font=("Arial", 10, "bold"))
        self.extract_btn.pack(side=tk.LEFT, padx=5)
        
        # Save text button
        self.save_btn = tk.Button(button_frame, text="Save as TXT", 
                                 command=self.save_text,
                                 bg="#f39c12", fg="white", padx=15, pady=8,
                                 font=("Arial", 10, "bold"))
        self.save_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_btn = tk.Button(button_frame, text="Clear Display", 
                                  command=self.clear_display,
                                  bg="#e74c3c", fg="white", padx=15, pady=8,
                                  font=("Arial", 10, "bold"))
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.status_label = tk.Label(content_frame, text="Ready", 
                                    bg="#ecf0f1", fg="#2c3e50",
                                    font=("Arial", 9), anchor="w")
        self.status_label.pack(fill=tk.X, pady=5, padx=5)
        
        # File list label
        file_label = tk.Label(content_frame, text="Selected Files:", 
                             bg="#f0f0f0", fg="#2c3e50",
                             font=("Arial", 10, "bold"))
        file_label.pack(anchor="w", padx=5)
        
        # File list frame with scrollbar
        file_frame = tk.Frame(content_frame, bg="white", height=80)
        file_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.file_listbox = tk.Listbox(file_frame, height=4, bg="white", 
                                       fg="#2c3e50", font=("Arial", 9))
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(file_frame, orient=tk.VERTICAL, 
                                 command=self.file_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)
        
        # Text display label
        text_label = tk.Label(content_frame, text="Extracted Text:", 
                             bg="#f0f0f0", fg="#2c3e50",
                             font=("Arial", 10, "bold"))
        text_label.pack(anchor="w", padx=5, pady=(10, 0))
        
        # Text display area
        self.text_display = scrolledtext.ScrolledText(content_frame, height=15, 
                                                      bg="white", fg="#2c3e50",
                                                      font=("Courier", 9),
                                                      wrap=tk.WORD)
        self.text_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#34495e", height=30)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_label = tk.Label(footer_frame, text="Created by Jaswanth | Advanced Python Project", 
                               bg="#34495e", fg="#ecf0f1", font=("Arial", 8))
        footer_label.pack(pady=5)
    
    def select_files(self):
        """Open file dialog to select PDF files."""
        files = filedialog.askopenfilenames(
            title="Select PDF File(s)",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        
        if files:
            self.selected_files = list(files)
            self.update_file_list()
            self.update_status(f"{len(self.selected_files)} file(s) selected")
            messagebox.showinfo("Success", f"Selected {len(self.selected_files)} PDF file(s)")
        else:
            self.update_status("No files selected")
    
    def update_file_list(self):
        """Update the file list display."""
        self.file_listbox.delete(0, tk.END)
        for file in self.selected_files:
            filename = os.path.basename(file)
            self.file_listbox.insert(tk.END, filename)
    
    def extract_text(self):
        """Extract text from selected PDF files."""
        if not self.selected_files:
            messagebox.showwarning("Warning", "Please select at least one PDF file first!")
            self.update_status("No files selected for extraction")
            return
        
        try:
            self.extracted_text = ""
            total_pages = 0
            
            for pdf_file in self.selected_files:
                with open(pdf_file, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    num_pages = len(pdf_reader.pages)
                    total_pages += num_pages
                    
                    # Add file header
                    self.extracted_text += f"\n{'='*80}\n"
                    self.extracted_text += f"File: {os.path.basename(pdf_file)}\n"
                    self.extracted_text += f"Pages: {num_pages}\n"
                    self.extracted_text += f"{'='*80}\n\n"
                    
                    # Extract text from each page
                    for page_num, page in enumerate(pdf_reader.pages, 1):
                        text = page.extract_text()
                        self.extracted_text += f"--- Page {page_num} ---\n"
                        self.extracted_text += text + "\n\n"
            
            # Display extracted text
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(1.0, self.extracted_text)
            
            msg = f"Successfully extracted text from {len(self.selected_files)} file(s) ({total_pages} pages total)"
            self.update_status(msg)
            messagebox.showinfo("Success", msg)
            
        except Exception as e:
            error_msg = f"Error extracting text: {str(e)}"
            self.update_status(error_msg)
            messagebox.showerror("Error", error_msg)
    
    def save_text(self):
        """Save extracted text to a file."""
        if not self.extracted_text:
            messagebox.showwarning("Warning", "No extracted text to save. Please extract text first!")
            self.update_status("No text to save")
            return
        
        try:
            # Suggest filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            default_name = f"extracted_text_{timestamp}.txt"
            
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
                initialfile=default_name
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.extracted_text)
                
                msg = f"Text saved successfully to {os.path.basename(file_path)}"
                self.update_status(msg)
                messagebox.showinfo("Success", msg)
            else:
                self.update_status("Save cancelled")
        
        except Exception as e:
            error_msg = f"Error saving file: {str(e)}"
            self.update_status(error_msg)
            messagebox.showerror("Error", error_msg)
    
    def clear_display(self):
        """Clear the text display and reset."""
        self.text_display.delete(1.0, tk.END)
        self.extracted_text = ""
        self.selected_files = []
        self.file_listbox.delete(0, tk.END)
        self.update_status("Display cleared")
        messagebox.showinfo("Success", "Display cleared and ready for new extraction")
    
    def update_status(self, message):
        """Update the status label."""
        self.status_label.config(text=f"Status: {message}")
        self.root.update()

def main():
    root = tk.Tk()
    app = PDFToTextConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
