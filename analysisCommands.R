

c <- read.csv('corpus-3DAnalysisByLine.csv')
c[order(-as.numeric(c$ZNorm)),]
cnotnull[order(-as.numeric(cnotnull$distFromPrev)),]
cnotnull[order(-as.numeric(cnotnull$ZNorm)),]

cnotnull <- c[c$distFromPrev != 'NULL',]
  
c[c$poem == 'NachtUndTraumeIPAMusic.txt',]
c[c$poem == 'DesBachesWiegenliedIPAMusic.txt',]
