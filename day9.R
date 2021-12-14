# determine all local minima of a 3d surface
rm(list=ls())
library(readr)

dat = read_file("data/day9test.txt")
lines = unlist(strsplit(dat,"\r\n"))

surf = list(rep(69, nchar(lines[1]) + 2))
for (l in lines) {
  # add a border of high numbers for testing the edges, 
  # we know each point is at most 9
  surf = c(surf, list(c(69, as.numeric(unlist(strsplit(l,""))), 69)))
}
surf = c(surf, list(rep(69, nchar(lines[1]) + 2)))
boo = surf[1:6] < surf[2:7]
