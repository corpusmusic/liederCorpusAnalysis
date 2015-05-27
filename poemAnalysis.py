# Python script for analyzing phonemic data from IPA-encoded poems

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

import codecs
import csv

# main variables

poemCorpus = ['NachtUndTraume.txt']
ignore = [' ', ':']
phonemeCategory = {
    'a': 'open',
    u'\u0061': 'open',
    'e': 'closeMid',
    u'\u025b': 'openMid',
    u'\u0259': 'none',
    'i': 'close',
    u'\u0049': 'close',
    'o': 'closeMid',
    u'\u0254': 'openMid',
    u'\u00f8': 'closeMid',
    u'\u0153': 'openMid',
    'y': 'close',
    u'\u0153': 'close',
    'u': 'close',
    u'\028a': 'close',
}
vowelTypes = ['open', 'close', 'none', 'openMid', 'closeMid']
phonemeCategoryList = list(set(phonemeCategory.values()))

# functions

def charactersInLine(poemContent, lineNumber):
    return len(poemContent[int(lineNumber) - 1])
    
def returnCharacter(poemContent, lineNumber, characterNumber):
    return poemContent[int(lineNumber) -1][int(characterNumber) - 1]


# script

for poem in poemCorpus:
    filename = poem
    name = filename.split('.')[0]
    content = [line.rstrip('\n') for line in codecs.open(filename, encoding='utf-8')]

    # basic information about the poem
    print name
    print "Number of lines:", len(content)
    i = 1
    for line in content:
        print "Line", str(i) + ":", len(line), "characters"
        i += 1
    
    # gather set of unicode characters
    unicodeSetRaw = []
    for line in content:
        for character in line:
            unicodeSetRaw.append(character)
    unicodeSet = set(unicodeSetRaw)
    
    # create empty unicodeCount dictionary
    unicodeCount = {}
    for phoneme in unicodeSet:
        unicodeCount[phoneme] = 0

    # create list to house data for writing to file
    
    outputData = []
    
    # count instances of each member of unicodeSet in poem
    for line in content:
        for character in line:
            unicodeCount[character] += 1

    # by line
    i = 1
    outputData = []
    outputDataProbability = []
    outputDataCategoryProbability = []

    while i <= len(content):
        label = 'Line ' + str(i)
        outputLine = []
        outputLineProbability = []
        outputLineCategoryProbability = []
        outputLine.append(label)
        outputLineCategoryProbability.append(label)
        outputLineProbability.append(label)
        rawTally = {}
        categoryTally = {}
        for phoneme in unicodeSet:
            rawTally[phoneme] = 0
        for category in phonemeCategoryList:
            categoryTally[category] = 0
        phonemeTotal = 0
        vowelTotal = 0

        for phoneme in content[i-1]:
            if phoneme not in ignore:
                phonemeTotal += 1
            rawTally[phoneme] += 1
            if phoneme in phonemeCategory.keys():
                categoryTally[phonemeCategory[phoneme]] += 1
                if phonemeCategory[phoneme] in vowelTypes:
                    vowelTotal += 1

        for phoneme in unicodeSet: 
            outputLine.append(rawTally[phoneme])
            outputLineProbability.append(float(rawTally[phoneme])/float(phonemeTotal))
        for category in phonemeCategoryList:
            outputLineCategoryProbability.append(float(categoryTally[category])/float(vowelTotal))

        i += 1
        outputData.append(outputLine)
        outputDataProbability.append(outputLineProbability)
        outputDataCategoryProbability.append(outputLineCategoryProbability)

    # write data to file - glyphs
    
    outputFileName = name + '-dataByGlyph.csv'
    with open(outputFileName, 'w') as csvfile:
        headerRow = []
        headerRow.append('Phoneme')
        for key in unicodeCount.keys():
            headerRow.append(key.encode('utf-8'))
            
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(headerRow)
        for row in outputData:
            w.writerow(row)
    print outputFileName, 'successfully created.'

    outputFileName = name + '-dataByGlyph-probability.csv'
    with open(outputFileName, 'w') as csvfile:
        headerRow = []
        headerRow.append('Phoneme')
        for key in unicodeCount.keys():
            headerRow.append(key.encode('utf-8'))
            
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(headerRow)
        for row in outputDataProbability:
            w.writerow(row)
    print outputFileName, 'successfully created.'

    outputFileName = name + '-dataByCategory-probability.csv'
    with open(outputFileName, 'w') as csvfile:
        headerRow = []
        headerRow.append('Category')
        for key in phonemeCategoryList:
            headerRow.append(key)
            
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(headerRow)
        for row in outputDataCategoryProbability:
            w.writerow(row)
    print outputFileName, 'successfully created.', '\n'



    # write data to file - categories
    
    outputFileName = name + '-dataByCategory.csv'
