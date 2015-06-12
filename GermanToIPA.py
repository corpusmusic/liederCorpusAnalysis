# -*- coding: utf-8 -*-

IPADict = {
    "Heil'ge": 'ha:Il.gə',
    'Nacht': 'naχt.',
    'du': 'du.',
    'sinkest': 'zIŋ.kəst',
    'nieder': 'ni.dəʁ'
}

def IPA(poemText, IPADict):
    IPATranslation = ''
    return IPATranslation


# test
print IPA("Heil'ge Nacht, du sinkest nieder;", IPADict) == u"ha:Il.gə naχt. du. zIŋ.kəst ni.dəʁ"