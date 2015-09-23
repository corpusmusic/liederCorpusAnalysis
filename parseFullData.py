# -*- coding: utf-8 -*-

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

from music21 import *
import csv
import fnmatch
import math
from os import listdir
from os import remove
# from phonemeDictionaries import phonemeCategoryNumbers as phonemeCategory
from phonemeDictionaries import phonemeCategoryFiveNumbers as phonemeCategory

sourceDirectory = 'textAndMusic'
destinationDirectory = 'parsedTextAndMusic'

vowelList = phonemeCategory.keys()

def vowelCategoryOfSyllable(syllable):
    for character in syllable:
        if character in vowelList:
            return phonemeCategory[character]
    return 'none'

def isStressed(syllable):
    if syllable[0] == "'":
        return "1" #stressed
    else:
        return "0" #unstressed

def beatStrength(noteBeat):
    if math.modf(noteBeat)[0] == 0.0:
        return 2
    if math.modf(noteBeat)[0] == 0.5:
        return 1
    else:
        return 0
    
def parseByNote(xmlsong):
    song = converter.parse(xmlsong)
    songOutput = []
    for note in song.flat.notes:
        if note.isGrace == False:
            noteOutput = []
            noteOutput.append(xmlsong.split('.')[0].split('/')[1])
            noteOutput.append(note.nameWithOctave)
            noteOutput.append(note.diatonicNoteNum)
            noteOutput.append(note.beat)
            noteOutput.append(beatStrength(note.beat))
            noteOutput.append(note.duration.quarterLength)
            noteOutput.append(note.lyric)
            noteOutput.append(vowelCategoryOfSyllable(note.lyric))
            noteOutput.append(isStressed(note.lyric))
            songOutput.append(noteOutput)
    return songOutput
    
def writeToCSV(dataToWrite, outputFileName):
    with open(outputFileName, 'w') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['song','pitch','diatonicNumber','beat','beatStrength','duration','IPA','vowelCategory','stress'])
        for row in dataToWrite:
            w.writerow(row)
    print outputFileName, 'successfully created.'

def appendToCSV(dataToWrite, outputFileName):
    with open(outputFileName, 'a') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        for row in dataToWrite:
            w.writerow(row)
    print outputFileName, 'successfully appended.'

poemCorpus = []
for file in listdir(sourceDirectory):
    if fnmatch.fnmatch(file, '*.xml'):
        poemCorpus.append(file)

if '00-corpus.csv' in listdir(destinationDirectory):
    remove(destinationDirectory + '/' + '00-corpus.csv')

if '00-corpus.csv' not in listdir(destinationDirectory):
    with open((destinationDirectory + '/' + '00-corpus.csv'), 'w') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['song','pitch','diatonicNumber','beat','beatStrength','duration','IPA','vowelCategory','stress'])
    

for filename in poemCorpus:
    destinationFilename = filename.split('.')[0] + '.csv'
    writeToCSV(parseByNote(sourceDirectory + '/' + filename), (destinationDirectory + '/' + destinationFilename))
    appendToCSV(parseByNote(sourceDirectory + '/' + filename), (destinationDirectory + '/' + '00-corpus.csv'))