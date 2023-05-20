import os
from pdf_processor import process_pdf_files

pdf_directory = '/home/aayam/check-pdf-blank/pdf'
blank_directory = '/home/aayam/check-pdf-blank/blank'

# Check if the PDF directory is empty
if not os.listdir(pdf_directory):
    print("PDF directory is empty.")
    exit()

# Process PDF files
process_pdf_files(pdf_directory, blank_directory)
