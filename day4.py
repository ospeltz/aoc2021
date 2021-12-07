# given a series of bingo cards and the order of the numbers called,
# determine which will win and which will lose

from funcs import read_file

data = read_file("day4_data.txt")

calls = data[0].split(",")

data = list(filter(lambda x: x != "", data[1:]))

def print_board(b):
    for bb in b:
        print(bb)
    print()
def print_boards(boards):
    for b in boards: print_board(b)

boards = []
board = []
while len(data) > 0:
    for i in range(5):
        board.append(list(filter(lambda x: x != "", data.pop(0).split(" "))))
    boards.append(board)
    board = []


def find_winner(loser=False):
    # pass loser = True to get the loser instead of the winner
    def getsum(b):
        s = 0
        for l in b:
            for x in l:
                if x[0] != "x": s += int(x)
        return s
    def checkboard(b):
        for i in range(5):
            if all(x[0] == "x" for x in b[i]): 
                return True
            if all(l[i][0] == "x" for l in b):
                return True
        return False

    for c in calls:
        for b in boards:
            for l in b:
                for n in range(len(l)):
                    if c == l[n]: l[n] = "x" + l[n]
        for b in boards:
            if loser:
                if checkboard(b) and len(boards) == 1: 
                    return getsum(b) * int(c)
                elif checkboard(b): 
                    boards.remove(b)
            else:
                if checkboard(b):
                    return getsum(b) * int(c)
        
win = find_winner(True)

print(win)



    
