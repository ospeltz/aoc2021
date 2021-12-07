# determine whether depth is increasing or decreasing given a string of readings
# using a one and 3 sliding window
from funcs import read_file


def part1():
    readings = read_file("day1_data.txt")

    inc = []
    for r1, r2 in zip(readings[:-1], readings[1:]):
        inc.append(r2>r1)

    print(inc)
    print(sum(inc))

def part2():
    with open("day1_data.txt","r") as f:
        win1 = []
        win2 = []
        for i in range(3):
            win1.append(int(f.readline()))
        win2 = win1[1:]
        inc = []
        for i, line in enumerate(f):
            win2.append(int(line))
            inc.append(sum(win2) > sum(win1))
            win1.pop(0)
            win1.append(int(line))
            win2.pop(0)
    print(sum(inc))

            


part2()

