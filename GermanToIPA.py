# -*- coding: utf-8 -*-

import codecs

IPADictTemp = {
    u'Heilge': u'ha:Il.gə',
    u'Nacht': u'naχt',
    u'du': u'du',
    u'sinkest': u'zIŋ.kəst',
    u'nieder': u'ni.dəʁ'
}

# import dictionary

IPADict = {}
translationDictionary = [line.rstrip('\n') for line in codecs.open('GermanIPADictionary.txt', encoding='utf-8')]
for entry in translationDictionary:
    x = entry.split(',')
    IPADict[x[0].lower()] = x[1]


punctuation = [ u".", u",", u":", u";", u"?", u"!", u"'", u"’", u'"', u"-", u"–", u"—" ]


def stripPunc(sourceFile, punctuation):
    content = [line.rstrip('\n') for line in codecs.open(sourceFile, encoding='utf-8')]
    strippedText = []
    for line in content:
        strippedLine = ''
        for letter in line:
            if letter not in punctuation:
                strippedLine += letter
        strippedText.append(strippedLine)
    
    return strippedText


def IPA(sourceText, IPADict):
    IPATranslation = []
    
    for line in sourceText:
        lineTranslation = u''

        # parse into list of words
        wordList = line.split()
    
        # replace words with IPA from dictionary
        for word in wordList:
            if word.lower() in IPADict.keys():
                lineTranslation += IPADict[word.lower()]
            else:
                lineTranslation += word
            lineTranslation += ' '
        lineTranslation = lineTranslation[:-1]
            
        IPATranslation.append(lineTranslation)
    
    return IPATranslation


def writeToFile(translation, filename):
    f = codecs.open(filename, mode='w', encoding='utf-8')
    for line in translation:
        f.write(line + '\n')
    f.close()
    print filename, 'successfully created.'


# run
sourceFile = 'NachtUndTraumeGerman.txt'
outputFile = 'NachtUndTraumeIPATemp.txt'
writeToFile(IPA(stripPunc(sourceFile, punctuation), IPADict), outputFile)