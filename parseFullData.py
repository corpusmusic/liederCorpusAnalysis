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

sourceDirectory = 'textAndMusic'
destinationDirectory = 'parsedTextAndMusic'

phonemeCategory = {
    'a': 0,
    'e': 2,
    u'\u025b': 0,
    u'\u0259': 1,
    'i': 2,
    'I': 2,
    u'\u026a': 2,
    'o': 2,
    u'\u0254': 0,
    u'\u00f8': 2,
    u'\u0153': 0,
    'y': 2,
    'u': 2,
    u'\u028a': 2,
    u'\u028f': 2,
}

phonemeCategoryFive = {
    'a': 'open',
    u'\u0061': 'open',
    'e': 'closeMid',
    u'\u025b': 'openMid',
    u'\u0259': 'neutral',
    'i': 'close',
    'I': 'close',
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