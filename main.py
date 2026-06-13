import math
from search import vectorChecking
from index import documents, index
# protoype

# vector searching




v = vectorChecking()

inputSearching = input('Input Search: ')
matches = []

for i in range(len(index)):
    relation = relation(v.word_count(inputSearching), index[i])
    if relation != 0:
        matches.append((relation,documents[i][:200]))

#ranking
matches.sort(reverse=True)


#displaying results
print(f"pending matches\n {matches[0]}\n{matches[1]}")


