import json

def saveFile(index):
    try:
        with open("dictionary.json", "w") as f:
            return json.dump(index, f)
    except ValueError as e:
        print(f'Error: the file is invalid json data. {e}')
    
def loadFile():
    try:
        with open('dictionary.json', 'r') as file:
            return json.load(file)
    except ValueError as e:
        print(f'Error: the file is invalid json data. {e}')
    

def savedocuments(documents):
    try:
        with open("documents.json", "w") as f:
            return json.dump(documents, f)
    except ValueError as e:
        print(f'Error: the file is invalid json data. {e}')