"""
@author: Nicolas R.
(c) 2020

"""
import os
import textProcessing
import tdIdf
import coOccurrence


if __name__ == '__main__':

    dataPath = "korpus/"
    documents = textProcessing.getAllTexts(dataPath) #documents = {filename: object with extracted info}

    coOccurences = coOccurrence.coOccurrenceMatrix(documents["korpus/baader_arbeit_1911.tcf.xml"], "Frauen")

    #td_idf = tdIdf.getTFIDF(documents)








"""
printer for ididf
for file in documents:
    print(documents[file].title)
    print(documents[file].author)
    print(documents[file].year)
    print(td_idf[file].get("Frauen")) #get returns None if word is not in file
    print()
"""






