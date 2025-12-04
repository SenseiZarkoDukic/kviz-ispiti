import PyPDF2
import sys

try:
    pdf_file = open('Osnove_fiziologije_sporta_2021.pdf', 'rb')
    reader = PyPDF2.PdfReader(pdf_file)
    
    full_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        full_text += f"\n\n=== PAGE {i+1} ===\n\n"
        full_text += text
    
    with open('pdf_content.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"Extracted {len(reader.pages)} pages")
    print(f"Total text length: {len(full_text)} characters")
    pdf_file.close()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

