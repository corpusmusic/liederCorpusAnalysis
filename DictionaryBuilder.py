# -*- coding: utf-8 -*-

import codecs
import csv
from GermanToIPA import stripPunc

GermanSourceFile = 'NachtUndTraumeGerman.txt'
IPASourceFile = 'NachtUndTraumeIPA.txt'

# wordify

def wordify(textAsListOfLists):
    wordifiedText = []
    for line in textAsListOfLists:
        wordList = line.split()
        wordifiedText.append(wordList)
    return wordifiedText

def wordCount(wordifiedText):
    totalWords = 0
    for line in wordifiedText:
        totalWords += len(line)
    return totalWords
    
# import dictionary

IPADict = {}
translationDictionary = [line.rstrip('\n') for line in codecs.open('GermanIPADictionary.txt', encoding='utf-8')]
for entry in translationDictionary:
    x = entry.split(',')
    IPADict[x[0].lower()] = x[1]

# import German text and IPA

GermanText = wordify(stripPunc(GermanSourceFile))
IPAText = wordify(line.rstrip('\n') for line in codecs.open(IPASourceFile, encoding='utf-8'))

if wordCount(GermanText) == wordCount(IPAText):
    i = 0
    for line in GermanText:
        j = 0
        for word in line:
            if word.lower() not in IPADict.keys():
                IPADict[word.lower()] = IPAText[i][j]
            j += 1
        i += 1
else:
    print "Error: German and IPA word counts do not match."
    print "German word count:", wordCount(GermanText)
    print "IPA word count:", wordCount(IPAText)

  
# write dict to CSV

with open('GermanIPADictionary-new.txt', 'w') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    for entry in IPADict.keys():
        rowToWrite = [entry.encode('utf-8'), IPADict[entry].encode('utf-8')]
        w.writerow(rowToWrite)
print 'GermanIPADictionary-new.txt', 'successfully created.'
