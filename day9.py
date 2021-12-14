from funcs import *
import numpy as np

dat = read_file("day9data.txt")
vals = np.array([[int(d) for d in l] for l in dat])

# create a border of 10s, max real value is 9
surf = np.ones((vals.shape[0]+2, vals.shape[1]+2)) * 10
vals_ind = (slice(1, surf.shape[0]-1), slice(1, surf.shape[1]-1))
surf[vals_ind] = vals

# compare each real value with its neighbors
up = surf[vals_ind] < surf[0:surf.shape[0]-2, vals_ind[1]]
down = surf[vals_ind] < surf[2:surf.shape[0], vals_ind[1]]
left = surf[vals_ind] < surf[vals_ind[0], 0:surf.shape[1]-2]
right = surf[vals_ind] < surf[vals_ind[0], 2:surf.shape[1]]

is_min = up & down & left & right

mins = vals[is_min]
vals[is_min] = -69 # make it obvious where they are

# part 1
# print(sum(mins+1))
def print_region(ind):
    # print the area around the region
    x0 = max(ind[0]-5, 0)
    x1 = min(ind[0]+5, vals.shape[0])
    y0 = max(ind[1]-5, 0)
    y1 = min(ind[1]+5, vals.shape[1])
    v = vals.copy()
    try:
        v[ind] = -99 # make it obvious what is the center
    except IndexError as e:
        pass
    print(v[x0:x1, y0:y1])

# part 2 identify basins that flow to the mins
def check_point(ind, u, d, l, r):
    # recursively adds up the number of points in a basin
    # print_region(ind)
    if ind[0] < 0 or ind[1] < 0 or ind[0] >= vals.shape[0] or ind[1] >= vals.shape[1] or vals[ind] == 9:
        # have reached an edge or a point already counted
        return 0
    vals[ind] = 9 # set to nine so not counted by other recursive branches
    s = 1
    if u and up[ind]:
        # check up and its neighbors
        s += check_point((ind[0]-1, ind[1]), True, False, True, True)
    if d and down[ind]:
        # check the neighbors down
        s += check_point((ind[0]+1, ind[1]), False, True, True, True)
    if l and left[ind]:
        # check neighbors to left
        s += check_point((ind[0], ind[1]-1), True, True, True, False)
    if r and right[ind]:
        # check neighbors to right
        s += check_point((ind[0], ind[1]+1), True, True, False, True)
    return s 

basins = []
min_ind = np.where(is_min) # get indices of minimums
for i in range(is_min.sum()):
    ind = (min_ind[0][i], min_ind[1][i])
    b = check_point(ind, True, True, True, True)
    basins.append(b)

basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])