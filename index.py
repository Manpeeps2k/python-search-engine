from pypdf import PdfReader
from pathlib import Path



def pdfParsing(fileName):
    text = PdfReader(fileName)
    extracted = ""

    for page in text.pages:
        extracted += page.extract_text() + "\n"

    return extracted

def folderScan():
    try:
        folder = Path(r'C:\Github-Projects\python-search-engine\documents')
        fileName = [file.name for file in folder.iterdir() if file.is_file()]
        return fileName
    except Exception as e:
        print(f'Inavlid, {e}')
    




# raw text
documents = {

}

# indexing data to dictionary
index = {

}
