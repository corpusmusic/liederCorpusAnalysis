# -*- coding: utf-8 -*-

import codecs
from DictionaryModules import stripPunc as stripPunc
from DictionaryModules import IPA as IPA
from DictionaryModules import writeToFile as writeToFile
from DictionaryModules import IPADict as IPADict

# run
sourceFile = 'HaltGerman.txt'
outputFile = 'HaltIPATemp.txt'
writeToFile(IPA(stripPunc(sourceFile), IPADict), outputFile)
