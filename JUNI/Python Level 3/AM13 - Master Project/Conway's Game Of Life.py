import time

file = input("Which file would you like to use? ")

grid = []
grid2 = []

for i in range(30):
    grid.append([])
    grid2.append([])
    for j in range(60):
        grid[i].append(False)
        grid2[i].append(False)

f = open(file + ".in", "r")

flist = f.readlines()

for i in flist:
    x = i.split()[0]
    y = i.split()[1]
    grid[int(x)][int(y)] = True
    grid2[int(x)][int(y)] = True

for i in grid:
    for j in i:
        if j == False:
            j = "-"
        else:
            j = "o"
        print(j, end='')
    print()


def neighbors(x, y):
    xend = len(grid2[y]) - 1
    yend = len(grid2) - 1
    alive = 0
    if y != 0 and x != 0:
        if grid2[y - 1][x - 1] == True:
            alive += 1
    if x != 0:
        if grid2[y][x - 1] == True:
            alive += 1
    if y != yend and x != 0:
        if grid2[y + 1][x - 1] == True:
            alive += 1
    if y != 0:
        if grid2[y - 1][x] == True:
            alive += 1
    if y != yend:
        if grid2[y + 1][x] == True:
            alive += 1
    if y != 0 and x != xend:
        if grid2[y - 1][x + 1] == True:
            alive += 1
    if x != xend:
        if grid2[y][x + 1] == True:
            alive += 1
    if y != yend and x != xend:
        if grid2[y + 1][x + 1] == True:
            alive += 1

    return alive


def rule1(x, y):
    alive = neighbors(x, y)
    if alive < 2:
        grid[y][x] = False
        global stop
        stop = True


def rule3(x, y):
    alive = neighbors(x, y)
    if alive > 3:
        grid[y][x] = False
        global stop
        stop = True


def rule4(x, y):
    alive = neighbors(x, y)
    if alive == 3:
        grid[y][x] = True
        global stop
        stop = True


stop = True

while True:
    stop = False
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == True:
                rule1(x, y)
                rule3(x, y)
            else:
                rule4(x, y)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid2[y][x] = grid[y][x]

    for y in grid:
        for x in y:
            if x == False:
                x = "-"
            else:
                x = "o"
            print(x, end='')
        print()

    time.sleep(0.25)