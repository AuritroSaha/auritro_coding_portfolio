import time

grid = []
grid2 = []

for i in range(10):
    grid.append([])
    grid2.append([])
    for j in range(10):
        grid[i].append(3)
        grid2[i].append(3)

p1 = open("player1.in", "r")
p2 = open("player2.in", "r")

p1list = p1.readlines()
p2list = p2.readlines()

for i in p1list:
    x = i.split()[0]
    y = i.split()[1]
    grid[int(x)][int(y)] = 1
    grid2[int(x)][int(y)] = 1

for i in p2list:
    x = i.split()[0]
    y = i.split()[1]
    grid[int(x)][int(y)] = 2
    grid2[int(x)][int(y)] = 2


def neighbors(x, y):
    X = 0
    O = 0
    xend = len(grid2[y]) - 1
    yend = len(grid2) - 1
    alive = 0
    majority = ""
    if y != 0 and x != 0:
        if grid2[y - 1][x - 1] != 3:
            alive += 1
            if grid2[y - 1][x - 1] == 1:
                X += 1
            else:
                O += 1
    if x != 0:
        if grid2[y][x - 1] != 3:
            alive += 1
            if grid2[y][x - 1] == 1:
                X += 1
            else:
                O += 1
    if y != yend and x != 0:
        if grid2[y + 1][x - 1] != 3:
            alive += 1
            if grid2[y + 1][x - 1] == 1:
                X += 1
            else:
                O += 1
    if y != 0:
        if grid2[y - 1][x] != 3:
            alive += 1
            if grid2[y - 1][x] == 1:
                X += 1
            else:
                O += 1
    if y != yend:
        if grid2[y + 1][x] != 3:
            alive += 1
            if grid2[y + 1][x] == 1:
                X += 1
            else:
                O += 1
    if y != 0 and x != xend:
        if grid2[y - 1][x + 1] != 3:
            alive += 1
            if grid2[y - 1][x + 1] == 1:
                X += 1
            else:
                O += 1
    if x != xend:
        if grid2[y][x + 1] != 3:
            alive += 1
            if grid2[y][x + 1] == 1:
                X += 1
            else:
                O += 1
    if y != yend and x != xend:
        if grid2[y + 1][x + 1] != 3:
            alive += 1
            if grid2[y + 1][x + 1] == 1:
                X += 1
            else:
                O += 1

    if X > O:
        majority = "X"
    else:
        majority = "O"

    return alive, majority


def printboard(grid):
    print("  0 1 2 3 4 5 6 7 8 9")
    row = 0
    for y in grid:
        print(str(row) + " ", end="")
        row += 1
        for x in y:
            if x == 3:
                x = "- "
            elif x == 2:
                x = "X "
            elif x == 1:
                x = "O "
            print(x, end='')
        print()


def rule1(x, y):
    alive, majority = neighbors(x, y)
    if alive < 2:
        grid[y][x] = 3
        global stop
        stop = True


def rule3(x, y):
    alive, majority = neighbors(x, y)
    if alive > 3:
        grid[y][x] = 3
        global stop
        stop = True


def rule4(x, y):
    global stop
    alive, majority = neighbors(x, y)
    if alive == 3:
        if majority == "X":
            grid[y][x] = 1
            stop = True
        else:
            grid[y][x] = 2
            stop = True


stop = True

player = 1

print("Player 1 is O and Player 2 is X\n\n")

printboard(grid)
print("\n\n")

while True:
    stop = False
    p1in = False
    p2in = False

    add = input("Player " + str(player) + "'s turn: " + "Give the coordinates that you want to make yours(ex: 1,3): ")
    kill = input("Player " + str(player) + "'s turn: " + "Give the coordinates that you want to kill(ex: 4,2): ")

    print("\n\n")

    add = add.replace(",", "")
    kill = kill.replace(",", "")
    add = add.replace(" ", "")
    kill = kill.replace(" ", "")

    if player == 1:
        grid[int(add[1])][int(add[0])] = 1
    else:
        grid[int(add[1])][int(add[0])] = 2

    grid[int(kill[1])][int(kill[0])] = 3

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid2[y][x] = grid[y][x]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1 or grid[y][x] == 2:
                rule1(x, y)
                rule3(x, y)
            else:
                rule4(x, y)

    printboard(grid)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                p1in = True
            elif grid[y][x] == 2:
                p2in = True

    if p1in == False:
        print("Player 2 wins!")
    elif p2in == False:
        print("Player 1 wins!")

    if player == 1:
        player = 2
    else:
        player = 1

    row = 0
    print("\n\n")
    time.sleep(0.25)