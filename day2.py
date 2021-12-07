# given a list of directions, determine the final location of the sub
def part1():
    x = 0
    d = 0

    with open("day2_data.txt","r") as f:
        for line in f:
            directions = line.split(" ")
            if directions[0] == "forward":
                x += int(directions[1])
            elif directions[0] == "down":
                d += int(directions[1])
            elif directions[0] == "up":
                d -= int(directions[1])
        
    print({x,d})
    print(x*d)

def part2():
    x = 0
    a = 0
    d = 0
    with open("day2_data.txt","r") as f:
        for line in f:
            directions = line.split(" ")
            if directions[0] == "forward":
                x += int(directions[1])
                d += int(directions[1]) * a
            elif directions[0] == "down":
                a += int(directions[1])
            elif directions[0] == "up":
                a -= int(directions[1])
    
    print(x, d)
    print(x*d)

part2()