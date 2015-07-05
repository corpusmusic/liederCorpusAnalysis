# -*- coding: utf-8 -*-

# Python script for building GermanIPADictionary.txt for use with GermanToIPA.py

# Copyright (C) 2015 Kris P. Shaffer

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

# ------------

# names of German and IPA source files to use for training
# edit this when running the script

GermanSourceFile = 'NachtUndTraumeGerman.txt'
IPASourceFile = 'NachtUndTraumeIPA.txt'

# do not change code below when running
# (unless you want to change the name of the output file in the last line)

import codecs
import csv
from GermanToIPA import stripPunc

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
