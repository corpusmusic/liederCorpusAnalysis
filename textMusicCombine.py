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
import codecs

musicDirectory = 'music'
textDirectory = 'texts'
musicFilename = 'DieLiebeFarbeMusic.xml'
textFilename = 'DieLiebeFarbeIPAMusic.txt'

def getText(directory, filename):
    return [line.rstrip('\n') for line in codecs.open((directory + '/' + filename), encoding='utf-8')]

def wholeSong(content):
    song = ''
    for line in content:
        if line != '':
            song += line
            song += ' '
    return song
    
def syllabify(songTextAsSingleString):
    return songTextAsSingleString.replace('.', ' ').split()
    
text = syllabify(wholeSong(getText(textDirectory, textFilename)))
s = converter.parse(musicDirectory + '/' + musicFilename)

for n in s.flat.notes:
    if n.getSpannerSites() == []:
        if text:
            n.lyric = text.pop(0)            
    else:
        ss = n.getSpannerSites()
        for thisSpanner in ss:
            if 'Slur' in thisSpanner.classes:
                if thisSpanner.isLast(n):
                    if text:
                        n.lyric = text.pop(0)
                else:
                    if text:
                        n.lyric = text[0]

s.write(fp='testXMLFile.xml')