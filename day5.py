# given a series of line segments, find the number of overlaps
# only consider horizontal, vertical, and diagonal lines
from funcs import *
data = read_file("day5data.txt")

segs = []
for l in data:
    p = l.split("->")
    p1 = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in p]

    segs.append(p1)


y_max = max(p[1] for l in segs for p in l)
x_max = max(p[0] for l in segs for p in l)

grid = [[0] * (y_max+1) for _ in range(x_max+1)]

for s in segs:
    
    x = [p[0] for p in s]
    y = [p[1] for p in s]
    if x[0] == x[1]:
        # horizontal
        for r in range(min(y), max(y)+1):
            grid[x[0]][r] += 1
    elif y[0] == y[1]:
        # vertical
        for r in range(min(x), max(x)+1):
            grid[r][y[0]] += 1
    elif abs(y[0]-y[1]) == abs(x[0]-x[1]):
        # diagonal
        print(s)
        for i in range(abs(x[0]-x[1]) + 1):
            xc = x[0] + i * (-1 * (x[1]<x[0])) + i * (1 * (x[1]>x[0]))
            yc = y[0] + i * (-1 * (y[1]<y[0])) + i * (1 * (y[1]>y[0]))
            grid[xc][yc] += 1
        
danger = sum(x > 1 for g in grid for x in g)
print(danger)