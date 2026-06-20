from search import vectorChecking
from index import documents, index, folderScan, pdfParsing
from file import saveFile, loadFile, savedocuments, loadDocuments

#load data
index = loadFile()
documents = loadDocuments()
v = vectorChecking()

while True:
    try:
        Choice = int(input("[1]Search\n[2]Scan Directory File(PDF)\n[3]Exit\nChoice: "))
    except ValueError:
        print("input number!")
        continue
    if Choice == 1:
        inputSearching = input('Input Search: ')
        matches = []
        vector_query = v.word_count(inputSearching.lower())

        for doc_id in index:
            relation = v.relation(vector_query, index[doc_id])
            if relation != 0:
                matches.append((relation,documents[doc_id][:70]))

        #ranking
        matches.sort(reverse=True)

        #displaying results
        if not matches:
            print("No matches found\n")
            continue

        print("pending matches\n")
        for match in matches:
            print(match, "\n")
            
    elif Choice == 2:
        try:
            count = 0
            fileNames = folderScan()

            for name in fileNames:
                pdfName = r'C:\Github-Projects\python-search-engine\documents\\' + name
                
                extracted_text = pdfParsing(pdfName)
                
                doc_id = str(len(documents))

                documents[doc_id] = str(extracted_text).lower()

                index[doc_id] = v.word_count(documents[doc_id])
                count += 1
            

            print(index.keys())
            print(documents.keys())
            print(f"Files ADDED, {count}")

            saveFile(index)
            savedocuments(documents)
        except Exception as e:
            print(f"Invalid! {e}")
            continue

        

    elif Choice == 3:
        print("Thank you!")
        break


