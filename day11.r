# model the flashing of octopuses' bioluminescent flashing that
# influences each other and synchronize
library(readr)
rm(list=ls())
lines <- unlist(strsplit(read_file("data/day11data.txt"), "\r\n"))
l <- as.numeric(unlist(strsplit(lines, "")))
data <- matrix(l, 10, 10, byrow = TRUE)
data_orig <- data

n_flashes <- 0
flash_triggered <- function(r, c, data, n_flashes) {
    # a flash is triggered at ind, increase all values adjacent by 1
    # returns a list of three 
    #   the first element indicates if any neighbors were pushed over 9
    #   the second is the updated data matrix
    #   the third is the count of cumulative number of flashes
    data[r, c] <- 0
    n_flashes <- n_flashes + 1

    neighbors <- rbind(
        c(r + 1, c), # down
        c(r - 1, c), # up
        c(r, c - 1), # left
        c(r, c + 1), # right
        c(r + 1, c + 1), # down right
        c(r + 1, c - 1), # down left
        c(r - 1, c + 1), # up right
        c(r - 1, c - 1)  # up left
    )
    boo <- FALSE
    for (i in 1:dim(neighbors)[1]) {
        if (all(neighbors[i, ] %in% 1:10) && 
            data[neighbors[i, 1], neighbors[i, 2]] != 0) {
            # if neighbor is valid point and the point there hasnt flashed
            data[neighbors[i, 1], neighbors[i, 2]] <-
                data[neighbors[i, 1], neighbors[i, 2]] + 1
            boo <- boo || data[neighbors[i, 1], neighbors[i, 2]] > 9
        }
    }
    return(list(boo, data, n_flashes))
}

n_steps <- 100
do_step <- function(data, n_steps) {
    # first increase all energy levels by 1
    data <- data + 1
    boo <- c(TRUE)
    while (any(boo)) {
        boo <- c(FALSE)
        # now any above 9 will 'flash' and increase the energy of those adjacent by 1
        inds <- which(data > 9, arr.ind=TRUE) # return indexes
        if (dim(inds)[1] == 0)
            next # skip to next step
        for (i in 1:dim(inds)[1]) {
            # for each initial flasher, update it neighbors, check if any
            # of its neighbors need to flash as well
            res <- flash_triggered(inds[i, 1], inds[i, 2], data, n_flashes)
          
            boo <- c(boo, res[[1]]) # use double brackets to "unlist"
            data <- res[[2]]
            n_flashes <- res[[3]]
        }
    }
    return (list(data, n_flashes))
}

# part 1, how many flashes after 100 steps
n_flashes = 0
for (st in 1:100) {
  res <- do_step(data, n_flashes)
  data <- res[[1]]
  n_flashes <- res[[2]]
}

# part 2, how long will it take to synchronize
n_steps <- 0
data <- data_orig
while (any(data != mean(data))) {
  n_steps <- n_steps + 1
  data <- do_step(data, 0)[[1]]
}

