from pypdf import PdfReader

def pdfParsing(fileName):

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
