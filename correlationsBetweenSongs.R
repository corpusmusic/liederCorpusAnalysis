## this needs some work to shorten song titles

allFiles <- list.files('statOutput', '*IPAMusic-wholeSongStressed.csv', full.names=TRUE)
corpus <- data.frame()
for(file in allFiles) {
    corpus <- rbind(corpus, read.csv(file))
}

row.names(corpus) <- allFiles    
correlations <- data.frame()
corpusSize <- nrow(corpus)

for(i in 1:corpusSize) {
    for(j in 1:corpusSize) {
        correlations[i,j] <- cor(as.numeric(corpus[i,]), as.numeric(corpus[j,]))
    }
}
row.names(correlations) <- allFiles    
## names(correlations) <- allFiles    ## these are too long, let's stick with numbers for now

means <- vector()

for(i in 1:corpusSize) {
    means[i] <- mean(as.numeric(correlations[i,1:corpusSize]))
}

write.csv(correlations, 'wholeCorpus-IPAMusic-songCorrelations-stressedVowels-Sep9.csv')
write.csv(corpus, 'wholeCorpus-IPAMusic-wholeSongStressed-Sep9.csv')