# liederCorpusAnalysis


[The Lieder Project](http://liederproject.shaffermusic.com/) — a research project of David Lonowski, Jordan Pyle, Stephen Rodgers, Kris Shaffer, and Leigh VanHandel. For an introduction to the project, please see our blog post, ["Getting Startet — The Lieder Project"](http://liederproject.shaffermusic.com/2015/getting-started-the-lieder-project).

The [texts](https://github.com/corpusmusic/liederCorpusAnalysis/tree/master/texts) folder contains a growing collection of German poems from prominent 19th-c. art songs and IPA (International Phonetic Alphabet) transcriptions of those songs. Songs have been transcribed using tools from [SIL](http://scripts.sil.org/cms/scripts/page.php?item_id=IPAhome).


The texts folder also contains a [German–IPA dictionary](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/texts/GermanIPADictionary.txt) and scripts for [auto-translating poems](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/texts/GermanToIPA.py) using the dictionary, and [adding new entries to the dictionary](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/texts/DictionaryBuilder.py) based on completed German–IPA transcriptions. See those scripts for use instructions, as well as two blog posts: ["Automatically translating German poetry to IPA"](http://liederproject.shaffermusic.com/2015/automatically-translating-german-poetry-to-ipa) and ["German-to-IPA Dictionary Builder."](http://liederproject.shaffermusic.com/2015/german-to-ipa-dictionary-builder)

The main folder contains the [poemAnalysis](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/poemAnalysis.py) Python script for analyzing IPA transcriptions of poems. This script analyzes the vowel content of each song in the corpus, categorizes vowels according to five categories (open, open-mid, neutral, close-mid, and close), and returns/outputs data about the probability of occurrence of those five vowel types for each song in the corpus — song-by-song, stanza-by-stanza, and line-by-line. Users can specify whether the script should analyze all vowels or only those in positions of stress (according to the poetic meter), and whether it should analyze both vowels in a diphthong or only the first (singers tend to sustain only the first vowel). For a more detailed description of what that script does, see [It works! — An update on the Lieder Project](http://liederproject.shaffermusic.com/2015/it-works-an-update-on-the-lieder-project).

The [statOutput folder](https://github.com/corpusmusic/liederCorpusAnalysis/tree/master/statOutput) contains the statistical output data of a recent run of poemAnalysis for all songs in the texts folder.

The main folder also contains [an R script](https://github.com/corpusmusic/liederCorpusAnalysis/blob/master/correlationsBetweenSongs.R) for performing a basic correlation analysis across all songs in the corpus, drawing on the whole-song phonemical data (stressed and unstressed, but only the first vowel of each diphthong — users can change parameters by changing the file-name filter in the first line of code).

# Documentation

To view IPA transcriptions, simply open the song file in this GitHub repository.

To run scripts, download the entire repository to your computer/server using 'git clone' or downloading the repository's zip file (click 'Download ZIP'). 

Currently, documentation consists of comments inside the scripts themselves, and a series of blog posts at [http://liederproject.shaffermusic.com/](http://liederproject.shaffermusic.com/). More detailed documentation coming in the future, as script development becomes more stable.


# Data management plan


One goal of The Lieder Project is to produce a corpus of phonetic transcriptions of poetry that can be contributed to by other researchers and musicians, and which can be used by other researchers and musical performers and teachers. The corpus of poems, as well as the code written to support its analysis, are intended to outlast the current research project, just as the project is drawing on an existing collection of musical transcriptions that were created in the course of an earlier project.


## Types of data produced

The primary data being assembled by The Lieder Project is a corpus of phonetic transcriptions of poetry that has been set to music. A published source for each poem is found and the text saved, each poem in its own plain-text file. A second plain-text file is created to contain the phonetic transcription of the song. These transcriptions are performed according to linguistic standards laid out in John Moriarty's Diction, and represented using symbols of the International Phonetic Alphabet (IPA), using standard UTF-8 text encoding. A third plain-text file is created for each poem, representing the phonetic text as it is set to music in a song in our musical corpus. (This mainly involves accounting for repetition, omission, or fragmentation of parts of the original poetry.)

These transcriptions are parsed by a script written in the Python programming language, which analyzes the text for certain phonemical characteristics and outputs the results in a series of comma-separated-values (CSV) plain-text files. These scripts are plain-text files, as well, with copious in-line comments provided to facilitate editing and reuse by ourselves and potential future users. 

Finally, we import musical data from plain-text files in the **kern format (one standard, text-based standard for musical data encoding). Using an open-source framework for the Python programming language, music21, we import the musical data into musicXML files (another, newer, musical encoding standard, also plain-text-based), in order to combine the musical and textual data of each song into a single file for comparative analysis. This analysis is also done using Python and/or the R programming language (using plain-text scripts), with results output as plain-text CSV files.


## Data and metadata standards

In the Lieder Project, all data and scripts are plain-text, human readable when possible and including copious in-line comments when not. No binary or proprietary formats are used in this project. The Lieder Project's data include poetic text, phonetic transcriptions of those texts (using the International Phonetic Alphabet, IPA), musical transcriptions (in kern format), scripts in the Python and R programming languages used to analyze that data, and statistical data resulting from that analysis. All data are housed in plain-text formats.

Metadata for each song are contained in the **kern source files: composer, composer's nationality, language of the text, title of the poem/song, title of the poem/song cycle, name of the poet, year composed, catalog numbers (such as a musical Opus number), and miscellaneous notes. 

Since the research team is using git and GitHub to coordinate our work (see below under Plans for archiving & preservation), metadata is automatically created and preserved regarding who performed the transcription, wrote the code, etc., down to the line of text. This version-control software also retains each version of the data, including the metadata about contributions made by researchers, even to earlier versions.


## Policies for access and sharing

All data is housed in a public repository on GitHub. The five current members of the research team are administrators for the repository. All users can find, view, copy, download the data, and all users can send "pull requests" (requests to contribute additions or changes to the repository), but only the five research team members currently have permission to alter this repository. Since we are currently exploring only poems and music written during the nineteenth century and earlier, all source material is in the public domain. All transcriptions and code we create are open-licensed (see below).


## Policies for re-use, redistribution

Since public use, reuse, and contribution are goals for The Lieder Project, all data is publicly housed and open-licensed. As mentioned above, all poetic and musical source material is in the public domain. Transcriptions that we create will be licensed with CC0 (the Creative Commons international equivalent of the public domain in the U.S.), and all software that we create is licensed with the GNU General Public License, v. 3.


## Plans for archiving & preservation

All data is preserved in plain-text file formats, to ensure wide compatibility both with current and with future technologies. Further, since git is a distributed version-control system, not only is the data housed on GitHub, a stable and easily accessible server, but the entirety of the project is also contained on multiple university-owned computers and backup drives (at CU, U of Oregon, and Michigan State), personal computers and backup drives belonging to members of the research team, and those belonging to anyone who creates or downloads a copy of the project on GitHub. Synchronization with the central repository is easy, both with the git command-line interface or the GitHub desktop applications. If/when the project reaches a terminal point or a major stable "release," a zipped copy of the plain-text data files and scripts will be submitted to CU Scholar (scholar.colorado.edu) for longer-term preservation.
