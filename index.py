from pypdf import PdfReader

def pdfParsing(fileName):
    if fileName != str:
        raise ValueError("Not valid input")
    
    text = PdfReader(fileName)
    extracted = ""

    for page in text.pages:
        extracted += page.extract_text() + "\n"

    return extracted

# raw text
documents = {

}

# indexing data to dictionary
index = {

}
