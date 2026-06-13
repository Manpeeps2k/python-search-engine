from search import vectorChecking
from index import documents, index, pdfParsing
from file import saveFile, loadFile

#load data
index = loadFile()

v = vectorChecking()

while True:
    Choice = int(input("[1]Search\n[2]Add PDF file\n[3]Exit"))
    if Choice == 1:
        inputSearching = input('Input Search: ')
        matches = []
        vector_query = v.word_count(inputSearching)

        for i in range(len(index)):
            relation = v.relation(vector_query, index[i])
            if relation != 0:
                matches.append((relation,documents[i][:200]))

        #ranking
        matches.sort(reverse=True)

        #displaying results
        if matches != None:
            print(f"pending matches\n {matches[0]}\n{matches[1]}")
        else:
            print("No Match Found!")
    
    elif Choice == 2:
        fileName = input("Add document File Name: ")
        parsedFile = pdfParsing(fileName)

        doc_id = len(documents)

        documents[doc_id] = parsedFile

        index[doc_id] = v.word_count(documents[id].lower())

    elif Choice == 3:
        print("Thank you!")
        saveFile(index) # save data
        break


