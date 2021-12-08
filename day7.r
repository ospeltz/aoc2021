# find the point that minimizing horizontal distance between 
# a bunch of crabs, note that this is absolute distance, not squared
# ie it is not just the average

rm(list=ls()) # clears all variables

crabs <- read.delim("data/day7data.txt", header=FALSE, ",")
crabs <- unlist(crabs, use.names=FALSE) # converts a list to a simple vector

abs.distance <- function(c, x) {
  # returns distance of each crab in c from point x using absolute value
  # part 1
  return (sum(abs(c - x)))
}
inc.distance <- function(c, x) {
  # returns distance of each crab in c from point x using nonlinear distance
  # part 2
  d = abs(c-x)
  return (sum(d*(d+1)/2))
}

find.min <- function(dist.func) {
  # dist.func should be a function that takes a list vector of ints and a point
  # and returns the total distance from that point
  # assumes dist.func has no maximum
  
  x0 <- round(sum(crabs) / length(crabs)) # start with average
  d0 <- dist.func(crabs, x0)
  
  flag = TRUE
  # descend from mean to true minimum
  while (flag) {
    dm = dist.func(crabs, x0-1)
    dp = dist.func(crabs, x0+1)
    if (dm > d0 && dp > d0) {
      flag = FALSE
      # found bottom
    } else if (dp < d0) {
      # go right
      x0 = x0 + 1
      d0 = dp
    } else if (dm < d0) {
      # go left
      x0 = x0 - 1
      d0 = dm
    } else {
      print("error")
      flag = FALSE
    }
  }
  return(d0)
}

part1 <- find.min(abs.distance)
part2 <- find.min(inc.distance)
