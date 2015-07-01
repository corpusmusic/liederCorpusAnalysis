# -*- coding: utf-8 -*-

IPADict = {
    "Heil'ge": 'ha:Il.gə',
    'Nacht': 'naχt.',
    'du': 'du.',
    'sinkest': 'zIŋ.kəst',
    'nieder': 'ni.dəʁ'
}

# replace test dictionary with import-from-CSV function

punctuation = [ ".", ",", ":", ";", "?", "!" "-", "–", "—" ]


def IPA(sourceText, IPADict):
    IPATranslation = ''
    
    # strip punctuation
    

    # parse into list of words
    # http://stackoverflow.com/questions/743806/split-string-into-a-list-in-python

    
    # replace words with IPA from dictionary (ignoring punctuation)

    
    # append words (and delimiting spaces) to IPATranslation

    
    return IPATranslation


# replace test text with import-from-TXT function



# test

GermanText = "Heil'ge Nacht, du sinkest nieder;"
IPAOutput = u"ha:Il.gə naχt. du. zIŋ.kəst ni.dəʁ"

print IPA(GermanText, IPADict) == IPAOutput