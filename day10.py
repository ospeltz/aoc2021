# parse a string of paired characters eg ()[]{}<> that can be nested and identify the bad syntax
from funcs import *

data = read_file("day10data.txt")

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
points2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]


# part 1 detect incorrect closing characters
# part 2 finish incomplete sequences
def scanLine(line):
    openPairs = []
    for i in range(len(line)):
        ch = line[i]
        if ch in openers:
            openPairs.append(ch)
        elif ch in closers:
            if len(openPairs) == 0:
                # invaldid closer
                print(ch, i)
                return ch
            elif openers.index(openPairs.pop()) != closers.index(ch):
                # invalid closer
                print(ch, i)
                return ch
    if len(openers) > 0: return openPairs
    else: return True

s1 = 0
s2 = []
for l in data:
    res = scanLine(l)
    if type(res) == str:
        # part 1
        s1 += points[res]
    elif type(res) == list:
        ss2 = 0
        while len(res) > 0:
            ss2 *= 5
            ss2 += points2[closers[openers.index(res.pop())]]
        s2.append(ss2)
print(s1)
s2.sort()
print(s2[len(s2) // 2])

