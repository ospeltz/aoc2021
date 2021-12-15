# given a list of connections between caves in a cave system, find all paths
# from 'start' to 'end' with some restrictions
from funcs import *

data = read_file("day12data.txt")

caves = {}

for con in data:
    cv = con.split("-")
    if cv[0] in caves:
        caves[cv[0]].add(cv[1])
    else:
        caves[cv[0]] = {cv[1]}
    if cv[1] in caves:
        caves[cv[1]].add(cv[0])
    else:
        caves[cv[1]] = {cv[0]}
    
            

# print_arr(data)
# print_map(caves)

paths = set()
path = ["start"]

def take_step(p, part2=False, special_cave=None):
    # explore all directions that you can go from current position in the path p
    # current position being the end
    # special_cave for part2: the name representing a small cave that can be visited twice 
    
    if not part2:
        # remove lower case caves if they have already been visited in this path
        legal_moves = [x for x in caves[p[-1]] if x.isupper() or x not in p]
    else:
        # remove lower case caves if they have been visited once, remove
        # special_cave if it has been visited twice
        legal_moves = [x for x in caves[p[-1]] 
                            if x.isupper() or 
                                x not in p or 
                                (x == special_cave and p.count(x) < 2)]

    for move in legal_moves:
        if move == 'end':
            paths.add(",".join([*p, move])) # save path as list for finding uniqueness
        else:
            if not part2:
                take_step([*p, move])
            else:
                take_step([*p, move], True, special_cave)

# part 1, find the number of paths to exit, only visiting lowercase caves once
# take_step(path)
# print_arr(paths)
# print(len(paths))

# part 2, you can visit a single lowercase cave twice in any given path
paths = set()
for sm in [x for x in caves if x.islower() and x != "start" and x != 'end']: # don't include 'start' as a special cave
    print(sm)
    take_step(['start'], True, sm)

print(len(paths))