## this needs some work to account for song titles
## will need to change once we have whole-song analysis method in Python script

allFiles <- list.files('statOutput/', '*categoryByStanza.csv', full.names=TRUE)
for(file in allFiles) {
    corpus <- rbind(corpus, read.csv(file))
}

correlations <- data.frame()

for(i in 1:20) {
    for(j in 1:20) {
        correlations[i,j] <- cor(as.numeric(corpus[i,]), as.numeric(corpus[j,]))
    }
}

means <- vector()

for(i in 1:20) {
    means[i] <- mean(as.numeric(correlations[i,1:20]))
}

means