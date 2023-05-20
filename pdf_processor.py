from PyPDF2 import PdfReader

def is_pdf_blank(file_path):
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        num_pages = len(pdf.pages)

        # Check each page for text or /XObject
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            text = page.extract_text()
            
            # If the page has non-blank text or /XObject, return False
            if text.strip() or '/XObject' in page:
                return False

        # If all pages are blank, return True
        return True

def process_pdf_files(pdf_directory, blank_directory):
    import os

    # Iterate over each file in the PDF directory
    for file_name in os.listdir(pdf_directory):
        file_path = os.path.join(pdf_directory, file_name)
        
        # Check if the file is a PDF
        if os.path.isfile(file_path) and file_name.lower().endswith('.pdf'):
            
            # Check if the PDF is blank
            if is_pdf_blank(file_path):
                # Move the PDF file to the blank directory
                os.rename(file_path, os.path.join(blank_directory, file_name))
