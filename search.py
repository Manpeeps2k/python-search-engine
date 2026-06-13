import math
#Querying

class vectorChecking:

    #calculating magnitude
    def magnitude(self, word_count):
        if type(word_count) != dict:
            raise ValueError('Supplied should be a dictionary')
        total = 0

        for word, count in word_count.items():
            total += count ** 2
        return math.sqrt(total)
    
    #calculating relation

    def relation(self, instance1,instance2):
        if type(instance1) != dict:
            raise ValueError('Instance is not a dictionary')
        if type(instance2) != dict:
            raise ValueError('Instance 2 is not a dictionary')
        top = 0

        for word, count in instance1.items():
            if instance2.has_key(word):
                top += count * instance2[word]
            if (self.magnitude(instance1) * self.magnitude(instance2) != 0):
                return top / (self.magnitude(instance1) * self.magnitude(instance2))
            else:
                return 0

    #tokenization
    def word_count(self, document):
        if type(document) != str:
            raise ValueError('Supplied should be a type of string')
        con = {}
        for word in document.split(' '):
            if word in con:
                con[word] = con[word] + 1 #adds instance of word
            else:
                con[word] = 1 #first instance
        return con