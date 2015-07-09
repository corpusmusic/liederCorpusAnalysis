# liederCorpusAnalysis

[The Lieder Project](http://liederproject.shaffermusic.com/) — a research project of David Lonowski, Jordan Pyle, Stephen Rodgers, Kris Shaffer, and Leigh VanHandel. For an introduction to the project, please see our blog post, ["Getting Startet — The Lieder Project."](http://liederproject.shaffermusic.com/2015/getting-started-the-lieder-project).

The [texts](https://github.com/corpusmusic/liederCorpusAnalysis/tree/master/texts) folder contains a growing collection of German poems from prominent 19th-c. art songs and IPA (International Phonetic Alphabet) transcriptions of those songs. Songs have been transcribed using tools from [SIL](http://scripts.sil.org/cms/scripts/page.php?item_id=IPAhome).


The texts folder also contains a [German–IPA dictionary](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/texts/GermanIPADictionary.txt) and scripts for [auto-translating poems](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/texts/GermanToIPA.py) using the dictionary, and [adding new entries to the dictionary](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/texts/DictionaryBuilder.py) based on completed German–IPA transcriptions. See those scripts for use instructions, as well as two blog posts: ["Automatically translating German poetry to IPA"](http://liederproject.shaffermusic.com/2015/automatically-translating-german-poetry-to-ipa) and ["German-to-IPA Dictionary Builder."](http://liederproject.shaffermusic.com/2015/german-to-ipa-dictionary-builder)

The main folder contains the [poemAnalysis](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/poemAnalysis.py) Python script for analyzing IPA transcriptions of poems. This script analyzes the vowel content of each song in the corpus, categorizes vowels according to five categories (open, open-mid, neutral, close-mid, and close), and returns/outputs data about the probability of occurrence of those five vowel types for each song in the corpus — song-by-song, stanza-by-stanza, and line-by-line. Users can specify whether the script should analyze all vowels or only those in positions of stress (according to the poetic meter), and whether it should analyze both vowels in a diphthong or only the first (singers tend to sustain only the first vowel). For a more detailed description of what that script does, see [It works! — An update on the Lieder Project](http://liederproject.shaffermusic.com/2015/it-works-an-update-on-the-lieder-project).

The [statOutput folder](https://github.com/corpusmusic/liederCorpusAnalysis/tree/master/statOutput) contains the statistical output data of a recent run of poemAnalysis for all songs in the texts folder.

The main folder also contains [an R script](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/correlationsBetweenSongs.R) for performing a basic correlation analysis across all songs in the corpus, drawing on the whole-song phonemical data (stressed and unstressed, but only the first vowel of each diphthong — users can change parameters by changing the file-name filter in the first line of code).

# Documentation

To view IPA transcriptions, simply open the song file in this GitHub repository.

To run scripts, download the entire repository to your computer/server using 'git clone' or downloading the repository's zip file (click 'Download ZIP'). 

Currently, documentation consists of comments inside the scripts themselves, and a series of blog posts at [http://liederproject.shaffermusic.com/](http://liederproject.shaffermusic.com/). More detailed documentation coming in the future, as script development becomes more stable.

