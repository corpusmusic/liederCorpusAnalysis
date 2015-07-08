# -*- coding: utf-8 -*-

# Python script for translating German text to IPA, using GermanIPADictionary.txt

# Copyright (C) 2015 Kris P. Shaffer, Jordan Pyle, David Lonowski

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import codecs
import csv

# import dictionary

IPADict = {}
translationDictionary = [line.rstrip('\n') for line in codecs.open('GermanIPADictionary.txt', encoding='utf-8')]
for entry in translationDictionary:
    x = entry.split(',')
    IPADict[x[0].lower()] = x[1]


def stripPunc(sourceFile):
    punctuation = [ u".", u",", u":", u";", u"?", u"!", u"'", u"’", u'"', u"-", u"–", u"—" ]
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
        lineTranslation = lineTranslation.replace('\r', '')
            
        IPATranslation.append(lineTranslation)
    
    return IPATranslation


def writeToFile(translation, filename):
    f = codecs.open(filename, mode='w', encoding='utf-8')
    for line in translation:
        f.write(line + '\n')
    f.close()
    print filename, 'successfully created.'



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
    
