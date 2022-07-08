# given a grid of numbers representing cost to move into that square, what is the minimum cost 
# to get from the top left to the bottom right of the grid?
# part two: what if the provided grid is just one tile of 25 in the full grid?
import heapq
import numpy as np


# read in data
with open("data/day15full.txt") as f:
    data = np.array([[int(c) for c in l if c != '\n'] for l in f.readlines()])
# data.shape = [y, x]

def city_block(yx, end):
    # return 'city block' distance to bottom right
    # use to estimate minimum cost to get from any square to the end square
    return abs(end[1]-yx[1]) + abs(end[0]-yx[0])

def get_neighbors(yx):
    # return an array of tuples (y,x) representing possible coordinates next to the provided point
    neighbors = [(yx[0]+1, yx[1]), (yx[0], yx[1]+1), (yx[0]-1, yx[1]), (yx[0], yx[1]-1)]
    return [i for i in neighbors if (i[0] in range(data.shape[0]) and i[1] in range(data.shape[1]))]

def reconstruct_path(current, start, came_from):
    # follow current along it's route to start
    path = [current]
    while current != start:
        current = came_from[current]
        path.insert(0, current)
    return path

def expand_grid(grid):
    # for part two
    # make a new grid 5 times the size, each 'tile' is the same as the given grid
    # but incremented 1, 9 wraps around to 1
    y, x = grid.shape
    new_grid = np.zeros((y*5, x*5))
    for i in range(5):
        for j in range(5):
            tile = (grid + i + j - 1) % 9 + 1
            new_grid[i*y:(i+1)*y, j*x:(j+1)*x] = tile
    return new_grid


# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def a_star(h):
    start = (0,0)
    goal = (data.shape[0]-1, data.shape[1]-1)
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # use a priority queue because it automatically sorts by the minimum cost 
    open_points = []
    heapq.heappush(open_points, (h(start, goal), start))

    # For point xy, came_from[xy] is the node immediately preceding it on the cheapest path from start
    # to xy currently known.
    came_from = {}

    # For node xy, g_score[xy] is the cost of the cheapest known path from start to xy
    g_score = {} # default value of inf
    g_score[start] = 0

    while len(open_points) > 0:
        _, current = heapq.heappop(open_points) # pops the node with the lowest g score
        if current == goal:
            # have reached end
            return (g_score[current], reconstruct_path(current, start, came_from))

        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_g_score is the distance from start to the neighbor through current
            tentative_g_score = g_score.get(current, np.Inf) + data[neighbor]
            if tentative_g_score < g_score.get(neighbor, np.Inf):
                # This path to neighbor is better than any previous one. Record it!
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_points, (tentative_g_score, neighbor))
                
    # Open set is empty but goal was never reached
    return "uh oh"

# part 1
# print(a_star(city_block)[0])

# part 2
data = expand_grid(data)
print(data.shape)


print(a_star(city_block)[0])
