# simulate an exponentially growing population of fish that are represented as
# daily decreasing integers, reproducing after 0

import time
from funcs import *
day0 = read_file("day6data.txt")[0]
fishies = [int(f) for f in day0.split(",")]

n_days = 256
immature = 8
mature = 6

    
def brute2():
    for _ in range(n_days):
        print(len(fishies))
        for f in range(len(fishies)):
            fishies[f] -= 1
            if fishies[f] < 0:
                fishies[f] = mature
                fishies.append(immature)
    print(len(fishies))

def smart():
    fish = [sum(f == i for f in fishies) for i in range(immature+1)]
    print(fish)
    for _ in range(n_days):
        bebes = fish.pop(0)
        fish.append(bebes)
        fish[mature] += bebes
        print(fish, sum(fish))

        
    print(sum(fish))

t0 = time.time()
smart()
print(time.time()-t0)



