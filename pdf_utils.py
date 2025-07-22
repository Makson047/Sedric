import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Витягує весь текст із PDF-файлу.
    """
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()