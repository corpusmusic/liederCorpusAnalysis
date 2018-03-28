library(tidyverse)

dsm <- read_csv('parsedTextAndMusic/00-corpus.csv') 


# musical functions

generic_interval <- function(lead, land) {
  return(land - lead)
}

pitch_class <- function(pitch) {
  pitch_name <- gsub('(\\d)', '', pitch)
  if (pitch_name %in% c('c', 'C', 'B#', 'B+', 'b#', 'b+')) {
    return(0)
  } else if (pitch_name %in% c('c#', 'C#', 'db', 'd-', 'Db', 'D-')) {
    return(1)
  } else if (pitch_name %in% c('d', 'D')) {
    return(2)
  } else if (pitch_name %in% c('d#', 'D#', 'eb', 'e-', 'Eb', 'E-')) {
    return(3)
  } else if (pitch_name %in% c('e', 'E', 'fb', 'f-', 'Fb', 'F-')) {
    return(4)
  } else if (pitch_name %in% c('e#', 'E#', 'f', 'F')) {
    return(5)
  } else if (pitch_name %in% c('f#', 'F#', 'gb', 'g-', 'Gb', 'G-')) {
    return(6)
  } else if (pitch_name %in% c('g', 'G')) {
    return(7)
  } else if (pitch_name %in% c('g#', 'G#', 'ab', 'a-', 'Ab', 'A-')) {
    return(8)
  } else if (pitch_name %in% c('a', 'A')) {
    return(9)
  } else if (pitch_name %in% c('a#', 'A#', 'bb', 'b-', 'Bb', 'B-')) {
    return(10)
  } else if (pitch_name %in% c('b', 'B', 'cb', 'c-', 'Cb', 'C-')) {
    return(11)
  } else {
    return(NA)
  }
}

octave <- function(pitch) {
  return(as.numeric(gsub('(\\D)', '', pitch)))
}

chromatic_pitch <- function(pitch) {
  return((12 * octave(pitch)) + pitch_class(pitch))
}

chromatic_interval <- function(lead, land) {
  return(land - lead)
}

# test

dsm_with_int <- dsm %>%
  mutate(gen_int = generic_interval(lag(diatonicNumber), diatonicNumber),
         chrom = mapply(chromatic_pitch, pitch),
         chrom_int = chromatic_interval(lag(chrom), chrom))

dsm_with_int %>%
  ggplot(aes(x = chrom,
             y = chrom_int)) +
  geom_jitter() +
  geom_smooth() +
  xlab('Chomatic pitch height (C4 = 48)') +
  ylab('Chromatic interval') +
  ggtitle('Relationship between chromatic pitch height and\nchromatic interval approaching target note in\nSchubert\'s Die schöne Müllerin')
