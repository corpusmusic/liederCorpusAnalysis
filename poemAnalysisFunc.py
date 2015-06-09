import codecs
import csv
import numpy


# line-by-line analysis

def poemAnalysisByLine(filename, categories, categoryDict, ignoreDiphthongs, threshold):
    ignore = [' ', ':']
    phonemeCategoryList = list(set(phonemeCategory.values()))
    name = filename.split('.')[0]
    content = [line.rstrip('\n') for line in codecs.open(filename, encoding='utf-8')]
    
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
    
    # count instances of each member of unicodeSet in poem
    for line in content:
        for character in line:
            unicodeCount[character] += 1
    
    # by line
    i = 1
    outputData = []
    outputDataProbability = []
    outputDataCategoryProbability = []

    print name + ':'

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
        j = 1 # character iterator

        for phoneme in content[i-1]:
            if phoneme not in ignore:
                phonemeTotal += 1
            rawTally[phoneme] += 1
            if phoneme in phonemeCategory.keys():
                print 'Line ' + str(i) + ', Character: ' + str(j) + ', ' + phoneme + ', ' + phonemeCategory[phoneme]
                if ignoreDiphthongs == False or content[i-1][j-2] != ':':
                    categoryTally[phonemeCategory[phoneme]] += 1
                    if phonemeCategory[phoneme] in vowelTypes:
                        vowelTotal += 1
            j += 1
                
        for phoneme in unicodeSet: 
            outputLine.append(rawTally[phoneme])
            outputLineProbability.append(float(rawTally[phoneme])/float(phonemeTotal))
        for category in phonemeCategoryList:
            outputLineCategoryProbability.append(float(categoryTally[category])/float(vowelTotal))

        i += 1
        outputData.append(outputLine)
        outputDataProbability.append(outputLineProbability)
        outputDataCategoryProbability.append(outputLineCategoryProbability)

    print '\n'

    # standard deviation
    
    meanLine = []
    meanLine.append('Mean')
    stDevLine = []
    stDevLine.append('StDev')
    j = 2 # columns
    columnTotal = len(outputDataCategoryProbability[0])
    rowTotal = len(outputDataCategoryProbability)
    timesExceedingThreshold = {}
    lineTransitionNames = []
    l = 1
    while l < rowTotal:
        lineTransitionNames.append('Line ' + str(l) + '-' + str(l+1))
        l += 1
    for item in lineTransitionNames:
        timesExceedingThreshold[item] = 0
    while j <= columnTotal:
        i = 1 # rows
        probabilities = []
        while i <= rowTotal:
            probabilities.append(outputDataCategoryProbability[i-1][j-1])
            i += 1
#        print 'Column ' + str(j) + ':', probabilities
#        print 'Mean:', numpy.mean(probabilities)
#        print 'StDev:', numpy.std(probabilities)

        # add mean, st dev to output
        meanLine.append(numpy.mean(probabilities))
        stDev = numpy.std(probabilities, dtype=numpy.float64)
        stDevLine.append(stDev)
        
        # Search for locations where line-to-line difference exceeds threshold
        k = 1
        while k < len(probabilities):
            if abs(probabilities[k] - probabilities[k-1]) >= stDev*threshold:
                print "Line " + str(k) + " to " + str(k+1) + ", " + phonemeCategoryList[j-2]
                timesExceedingThreshold['Line ' + str(k) + '-' + str(k+1)] += 1
            k += 1
        
        j += 1
    
    print '\n'
    for key in lineTransitionNames:
        print key + ':', timesExceedingThreshold[key], 'categories exceed the threshold.'
    print '\n'

    outputDataCategoryProbability.append(meanLine)
    outputDataCategoryProbability.append(stDevLine)
    

    # write data to file - glyphs
    
    outputFileName = name + '-dataByGlyph.csv'
    with open(outputFileName, 'w') as csvfile:
        headerRow = []
        headerRow.append('Phoneme')
        for phoneme in unicodeSet:
            headerRow.append(phoneme.encode('utf-8'))
            
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(headerRow)
        for row in outputData:
            w.writerow(row)
    print outputFileName, 'successfully created.'

    outputFileName = name + '-dataByGlyph-probability.csv'
    with open(outputFileName, 'w') as csvfile:
        headerRow = []
        headerRow.append('Phoneme')
        for phoneme in unicodeSet:
            headerRow.append(phoneme.encode('utf-8'))
            
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

    print '\n'

    


# main variables

poemCorpus = ['NachtUndTraumeIPA.txt', 'WohinIPA.txt', 'DasWandernIPA.txt']
vowelTypes = ['close', 'closeMid', 'neutral', 'openMid', 'open']
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
    
# run it

for poem in poemCorpus:
    poemAnalysisByLine(poem, categories=vowelTypes, categoryDict=phonemeCategory, ignoreDiphthongs=True, threshold=2)
