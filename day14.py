# simulate a replicating polymer and find the counts of elements
# after n replication steps
from funcs import *
import time

data = read_file("day14data.txt", remove_blanks=True)

poly = data[0]
mapping = {}
elms = {} # unique elements

for l in data[1:]:
    l = l.split(" -> ")
    if l[0] in mapping:
        print('warning: maps not unique')
    elms[l[0][0]] = 0
    elms[l[0][1]] = 0
    elms[l[1]] = 0

    mapping[l[0]] = l[0][0] + l[1] + l[0][1]

def dumb(n_steps, poly):
    # conduct n_steps of polymerization, saves as a string which becomes unmanageable after 
    # more than 18 steps (time doubles every step)
    for n in range(n_steps):
        t0 = time.time()
        new_poly = ""
        for i in range(len(poly)-1):
            if poly[i:i+2] in mapping:
                if new_poly == "":
                    # keep first character
                    new_poly = mapping[poly[i:i+2]]
                else:
                    # throw out first character (it is included in previous pair)
                    new_poly += mapping[poly[i:i+2]][1:]
        poly = new_poly

    counts = []
    for e in elms:
        counts.append(poly.count(e))
    print_map(counts)
    print(counts[-1] - counts[0])

# part 1: find most and least common elements after 10 steps
dumb(10, "NN")
    
def smart(n_steps, poly):
    # conduct n_steps of polymerization, we only care about the count of pairs
    # and we don't care about the location either
    pairs = [a+b for a, b in zip(poly[:-1], poly[1:])]
    counts = {}
    for p in pairs:
        if p in counts:
            counts[p] += 1
        else:
            counts[p] = 1
    for _ in range(n_steps):
        newCounts = {k : 0 for k in mapping.keys()}
        for p in counts:
            new = mapping[p]
            newCounts[new[:2]] += counts[p]
            newCounts[new[1:]] += counts[p]
        counts = newCounts
    # count up the individual letters
    for p in counts:
        elms[p[0]] += counts[p]
    # last letter in starting seq gets extra
    elms[poly[-1]] += 1
    print(max(elms[k] for k in elms) - min(elms[k] for k in elms))

smart(40, poly)

            
            
            