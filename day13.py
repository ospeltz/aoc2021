# fold some paper and see what number it makes
from funcs import *
import numpy as np

data = read_file("day13data.txt", remove_blanks=True)

folds = [x for x in data if "fold along" in x]
points = [x.split(",") for x in data if "fold along" not in x]

x_max = 0
y_max = 0

for i in range(len(points)):
    points[i] = (int(points[i][1]), int(points[i][0])) # reverse order
    if points[i][1] > x_max: x_max = points[i][1]
    if points[i][0] > y_max: y_max = points[i][0]

sheet = np.zeros((y_max+1, x_max+1))
for p in points:
    sheet[p] = 10

print(sheet.shape)

def fold_sheet(sht, axis, i):
    # fold the sheet either horizontally or vertically and return it
    i = int(i)
    axis = int(axis == 'x')
    if sht.shape[axis] // 2 != i:
        print('warning: fold not along middle. sht = {}, {} = {}'.format(sht.shape, axis, i))

    if not axis:
        # fold horizontally
        half1 = sht[:i, :]
        half2 = sht[sht.shape[0]-1:i:-1, :]
    else:
        # fold vertically
        half1 = sht[:, :i]
        half2 = sht[:, sht.shape[1]-1:i:-1]

    # line up halfs if not down middle
    diff = half1.shape[axis] - half2.shape[axis]
    if diff > 0:
        if axis:
            half2 = np.concatenate((np.zeros((half2.shape[0], diff)), half2), axis)
        else:
            half2 = np.concatenate((np.zeros((diff, half2.shape[1])), half2), axis)
    elif diff < 0:
        if axis:
            half1 = np.concatenate((half1, np.zeros((half1.shape[0], abs(diff)))), axis)
        else:
            half1 = np.concatenate((half1, np.zeros((abs(diff), half1.shape[1]))), axis)

    return half1 + half2

for f in folds:
    f = f.replace("fold along ", "").split("=")
    sheet = fold_sheet(sheet, *f)
    print((sheet == 0).sum(), (sheet > 0).sum())
    print()


for i in range(sheet.shape[0]):
    l = ""
    for j in range(sheet.shape[1]):
        if sheet[i,j] > 0:
            l += "#"
        else:
            l += "."
    print(l)


