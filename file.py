import json

def saveFile(index):
    try:
        with open("dictionary.json", "w") as f:
            return json.dump(index, f)
    except ValueError as e:
        print(f'Error: the file is invalid json data. {e}')
    
def loadFile(index):
    try:
        with open('dictionary.json', 'r') as file:
            index = json.load(file)
            return index
    except ValueError as e:
        print(f'Error: the file is invalid json data. {e}')
    