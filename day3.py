# determine some meta numbers from a sequence of binary numbers based on the 
# most common or uncommon bits in that position
from funcs import read_file

data = read_file("day3data.txt")

def most_common(dat):
    # dat is a list of binary strings of the same length
    # x is 0 or 1 for whether a 0 or 1 should be preferred in the case of ties
    gamma = []
    for line in dat:
        if len(gamma) == 0:
            for d in line:
                gamma.append(int(d))
        else:
            for i in range(len(line)):
                gamma[i] += int(line[i])

    g = ""
    for d in gamma:
        if d == len(dat)/2 : g += "1"
        else: g += str(round(d / len(dat)))
    return g
    
def part1():
    gamma = []

    g = most_common(data)
    e = g.translate(str.maketrans("10","01"))

    print(g, int(g,2))
    print(e, int(e,2))

    print(int(g,2) * int(e,2))

def part2(x):
    res = data.copy()
    i = 0
    while len(res) > 1 or len(set(res)) > 1: # if more than one unique value
        g = most_common(res)
        if x == "0":
            g = g.translate(str.maketrans("10","01"))
        
        res = list(filter(lambda line: line[i] == g[i], res))
        i += 1
    
    return int(res[0],2)


a = part2("0")
b = part2("1")

print(a,b,a*b)

