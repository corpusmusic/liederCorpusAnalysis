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
import numpy

class IPAText(object):
    
    def __init__(self, filename):
        self.filename = filename
        self.name = filename.split('.')[0]
        self.content = [line.rstrip('\n') for line in codecs.open(self.filename, encoding='utf-8')]
    
    def unicodeSet(self):
        unicodeSetRaw = []
        for line in self.content:
            for character in line:
                unicodeSetRaw.append(character)
        return set(unicodeSetRaw)

    def unicodeDictionary(self):
        unicodeCount = {}
        for phoneme in self.unicodeSet():
            unicodeCount[phoneme] = 0
        for line in self.content:
            for member in line:
                unicodeCount[member] += 1
        return unicodeCount
            
    def unicodeCount(self,character):
        unicodeCount = {}
        for phoneme in self.unicodeSet():
            unicodeCount[phoneme] = 0
        for line in self.content:
            for member in line:
                unicodeCount[member] += 1
        return unicodeCount[character]

    def parseGlyphByLine(self):
        i = 1
        outputData = []
        headerRow = []
        headerRow.append('Phoneme')
        for phoneme in self.unicodeSet():
            headerRow.append(phoneme.encode('utf-8'))
        outputData.append(headerRow)
        while i <= len(self.content):
            label = 'Line ' + str(i)
            outputLine = []
            outputLine.append(label)
            rawTally = {}
            categoryTally = {}
            for phoneme in self.unicodeSet():
                rawTally[phoneme] = 0
            phonemeTotal = 0

            j = 1 # character iterator
            for phoneme in self.content[i-1]:
                phonemeTotal += 1
                rawTally[phoneme] += 1
                j += 1

            for phoneme in self.unicodeSet(): 
                outputLine.append(rawTally[phoneme])

            i += 1
            outputData.append(outputLine)
        return outputData

    def parseCategoryProbByLine(self, ignore, categoryDictionary, ignoreDiphthongs):
        i = 1
        outputDataCategoryProbability = []
        phonemeCategoryList = list(set(categoryDictionary.values()))

        while i <= len(self.content):
            label = 'Line ' + str(i)
            outputLineCategoryProbability = []
            outputLineCategoryProbability.append(label)
            rawTally = {}
            categoryTally = {}
            for phoneme in self.unicodeSet():
                rawTally[phoneme] = 0
            for category in phonemeCategoryList:
                categoryTally[category] = 0
            phonemeTotal = 0
            categoryMemberTotal = 0

            j = 1 # character iterator
            for phoneme in self.content[i-1]:
                if phoneme not in ignore:
                    phonemeTotal += 1
                rawTally[phoneme] += 1
                if phoneme in phonemeCategory.keys():
                    if ignoreDiphthongs == False or self.content[i-1][j-2] != ':':
                        categoryTally[phonemeCategory[phoneme]] += 1
                        if phonemeCategory[phoneme] in phonemeCategoryList:
                            categoryMemberTotal += 1
                j += 1
            for category in phonemeCategoryList:
                outputLineCategoryProbability.append(float(categoryTally[category])/float(categoryMemberTotal))

            i += 1
            outputDataCategoryProbability.append(outputLineCategoryProbability)
            
        meanLine = []
        meanLine.append('Mean')
        stDevLine = []
        stDevLine.append('StDev')
        j = 2 # columns
        columnTotal = len(outputDataCategoryProbability[0])
        rowTotal = len(outputDataCategoryProbability)
        while j <= columnTotal:
            i = 1 # rows
            probabilities = []
            while i <= rowTotal:
                probabilities.append(outputDataCategoryProbability[i-1][j-1])
                i += 1
            meanLine.append(numpy.mean(probabilities))
            stDev = numpy.std(probabilities, dtype=numpy.float64)
            stDevLine.append(stDev)
            j += 1
        
        outputDataCategoryProbability.append(meanLine)
        outputDataCategoryProbability.append(stDevLine)

        return outputDataCategoryProbability

    


     
def writeToCSV(dataToWrite, outputFileName):
    with open(outputFileName, 'w') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        for row in dataToWrite:
            w.writerow(row)
    print outputFileName, 'successfully created.'
    
    
# testing area

ignore=['.', ':', ' ']
phonemeCategory = {
    'a': 'open',
    u'\u0061': 'open',
    'e': 'closeMid',
    u'\u025b': 'openMid',
    u'\u0259': 'neutral',
    'i': 'close',
    'I': 'open',
#    u'\u026a': 'close',
    'o': 'closeMid',
    u'\u0254': 'openMid',
    u'\u00f8': 'closeMid',
    u'\u0153': 'openMid',
    'y': 'close',
    u'\u0153': 'close',
    'u': 'close',
    u'\028a': 'close',
}

poemCorpus = ['NachtUndTraumeIPA.txt', 'WohinIPA.txt', 'DasWandernIPA.txt']
nacht = IPAText('NachtUndTraumeIPA.txt')
ignoreOptions = [True, False]
for option in ignoreOptions:
    writeToCSV(nacht.parseCategoryProbByLine(ignore, phonemeCategory, option), (nacht.name + str(option) + '-testOutput.csv'))