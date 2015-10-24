corpus <- data.frame()
corpus <- read.csv('ParsedTextAndMusic/00-corpus.csv')
features <- colnames(corpus)
songlist <- unique(corpus$song)
correlations <- data.frame()

for(x in 1:length(songlist)) {
  songdata <- data.frame(song)
  songdata <- subset(corpus, corpus$song == songlist[[x]])
  pitchCorr <- cor(as.numeric(songdata$diatonicNumber), as.numeric(songdata$vowelCategory))
  beatCorr <- cor(as.numeric(songdata$beat), as.numeric(songdata$vowelCategory))
  beatStrengthCorr <- cor(as.numeric(songdata$beatStrength), as.numeric(songdata$vowelCategory))
  durCorr <- cor(as.numeric(songdata$duration), as.numeric(songdata$vowelCategory))
  stressCorr <- cor(as.numeric(songdata$stress), as.numeric(songdata$vowelCategory))
  dataRow <- data.frame()
  dataRow <- c(as.factor(songlist[[x]]), as.numeric(pitchCorr), as.numeric(beatCorr), as.numeric(beatStrengthCorr), as.numeric(durCorr), as.numeric(stressCorr))
  
  correlations <- rbind(correlations, dataRow)
}

colnames(correlations) <- c('song', 'pitch', 'beat', 'beatStrength', 'duration', 'stress')
correlations