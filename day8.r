# day 8: given a sequence of letters representing the 10 digits
# on a  7 segment clock, figure out which digit is which
rm(list=ls())
dat <- read.delim("data/day8data.txt", header=FALSE, sep="|")

output <- strsplit(trimws(dat$V2), " ") # trim spaces, split on space
codes  <- strsplit(trimws(dat$V1), " ")

set.contains <- function(x,y) {
  # return true if all of the characters in y are in x
  # both should be strings
  boo = TRUE
  y = unlist(strsplit(y, ""))
  for (c in y) {
    boo = boo && (grepl(c, x)==1)
  }
  return (boo)
}
# allow a whole vector to be tested at once
sets.contain <- Vectorize(set.contains, "x") 

count.ifs = c(2, 5, 8, 9) # +1 the true value
count = 0
big.sum = 0

for (j in 1:length(codes)) {
  # generate map
  seq = unlist(codes[j])
  nmap = rep("", 10) # code representing 0 at index 1 and so on
  # identify gimmes
  for (i in 1:length(seq)) {
    # sort the code
    seq[i] = paste(sort(unlist(strsplit(seq[i], ""))), collapse = "")
    if (nchar(seq[i]) == 2) {
      # must represent 1
      nmap[2] = seq[i]
    } else if (nchar(seq[i]) == 7) {
      # must represent 8
      nmap[9] = seq[i]
    } else if (nchar(seq[i]) == 4) {
      # must represent 4
      nmap[5] = seq[i]
    } else if (nchar(seq[i]) == 3) {
      # must represent 7
      nmap[8] = seq[i]
    }
  }
  zeroSixNine = seq[nchar(seq) == 6] # all use 6 segments
  twoThreeFive = seq[nchar(seq) == 5] # all use 5 segments
  # zero contains all of 7 but not all of 4, nine contains all of both
  nmap[1]  = zeroSixNine[sets.contain(zeroSixNine, nmap[8]) & !sets.contain(zeroSixNine, nmap[5])]
  nmap[10] = zeroSixNine[sets.contain(zeroSixNine, nmap[8]) &  sets.contain(zeroSixNine, nmap[5])]
  nmap[7]  = zeroSixNine[!sets.contain(zeroSixNine, nmap[8])]
  # three contains all of 1, 2 and 5 do not
  three = sets.contain(twoThreeFive, nmap[2])
  nmap[4] = twoThreeFive[three]
  # six contains 5 but not 2 or 3
  five = rep(FALSE, 3)
  for (i in 1:length(twoThreeFive)) {
    five[i] = set.contains(nmap[7], twoThreeFive[i])
  }
  nmap[6] = twoThreeFive[five]
  nmap[3] = twoThreeFive[!three & !five]
  
  # map output and count numbers of interest, sum up total
  nums = unlist(output[j])
  s = 0
  f = 1000
  for (n in nums) {
    # sort the code
    n = paste(sort(unlist(strsplit(n, ""))), collapse = "")
    ind = which(nmap==n)
    s = s + f * (ind - 1)
    f = f / 10
    if (ind %in% count.ifs) {
      count = count + 1
    }
  }
  big.sum = big.sum + s
}
