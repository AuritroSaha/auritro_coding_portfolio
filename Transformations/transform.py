"""
ID: roobeel1
LANG: PYTHON3
TASK: transform
"""
import copy
f = open("transform.in", "r")

values = [x.strip() for x in f.readlines()]

dimensions = int(values[0])

originalGrid = []
transformedGrid = []
for i in range(1, 1 + dimensions):
    originalGrid.append([x for x in values[i]])
    transformedGrid.append([x for x in values[i + dimensions]])


def degree90(grid, dimension):
    newgrid = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            row.append(0)
        newgrid.append(row)

    for i in range(dimension):
        for j in range(dimension):
            newgrid[j][-i - 1] = grid[i][j]
    return newgrid


def degree180(grid, dimension):
    for i in range(2):
        grid = degree90(grid, dimension)
    return grid


def degree270(grid, dimension):
    for i in range(3):
        grid = degree90(grid, dimension)
    return grid

def reflection(grid, dimension):
    newgrid = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            row.append(0)
        newgrid.append(row)

    for i in range(dimension):
        for j in range(dimension):
            newgrid[i][-j - 1] = grid[i][j]

    return newgrid

def combo(grid, dimension):
    newgrid = reflection(grid, dimension)
    for i in range(3):
        newgrid = degree90(newgrid, dimension)
        if newgrid == transformedGrid:
            return True
    return False

f = open("transform.out", "w")

#
# a = 5
# b = a
# b = 10
# print(a)
# print(b)
# a = [[1, 2, 3]]
# b = a
# #b = copy.deepcopy(a)
# b[0] = 60
# print(a)
# print(b)

if degree90(originalGrid, dimensions) == transformedGrid:
    f.write("1\n")

elif degree180(originalGrid, dimensions) == transformedGrid:
    f.write("2\n")

elif degree270(originalGrid, dimensions) == transformedGrid:
    f.write("3\n")

elif reflection(originalGrid, dimensions) == transformedGrid:
    f.write("4\n")

elif combo(originalGrid, dimensions):
    f.write("5\n")

elif originalGrid == transformedGrid:
    f.write("6\n")

else:
    f.write("7\n")

# you are not allowed to numpy because if you do, the autogarder will not compile your code
# if you write a method for 90 degree clockwise rotation, you do not need to write methods for 180 or 270 degree rotation, just reuse
