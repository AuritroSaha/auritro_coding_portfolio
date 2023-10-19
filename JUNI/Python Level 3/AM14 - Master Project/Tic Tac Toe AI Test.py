import random

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def printgrid(grid):
    print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
    print("---+---+---")
    print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
    print("---+---+---")
    print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])


winner = ""


def win(key, grid):
    for i in range(len(grid)):
        row = grid[i]
        vert1 = grid[0][i]
        vert2 = grid[1][i]
        vert3 = grid[2][i]

        if row[0] == row[1] == row[2] == key:
            return True
        elif vert1 == vert2 == vert3 == key:
            return True

    if grid[0][0] == grid[1][1] == grid[2][2] == key:
        return True
    elif grid[2][0] == grid[1][1] == grid[0][2] == key:
        return True

    return False


def ai():
    tempgrid = []
    for i in grid:
        temp = []
        for j in i:
            temp.append(j)
        tempgrid.append(temp)

    # trying to win
    for j in range(len(tempgrid)):
        for i in range(len(tempgrid[j])):
            if tempgrid[j][i] != "X" and tempgrid[j][i] != "O":
                tempgrid[j][i] = "O"
                if win("O", tempgrid):
                    return [j, i]
                tempgrid = []
                for y in grid:
                    temp = []
                    for x in y:
                        temp.append(x)
                    tempgrid.append(temp)

    # trying to block
    for j in range(len(tempgrid)):
        for i in range(len(tempgrid[j])):
            if tempgrid[j][i] != "X" and tempgrid[j][i] != "O":
                tempgrid[j][i] = "X"
                if win("X", tempgrid):
                    return [j, i]
                tempgrid = []
                for y in grid:
                    temp = []
                    for x in y:
                        temp.append(x)
                    tempgrid.append(temp)

    # trying to place next to eachother
    for j in range(len(tempgrid)):
        for i in range(len(tempgrid[j])):
            if tempgrid[j][i] == "O":
                off = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                for k in range(len(off)):
                    y = j + off[k][1]
                    x = i + off[k][0]
                    if x < 3 and x > -1 and y < 3 and y > -1 and tempgrid[y][x] == " ":
                        return [y, x]

    # random placment(for first turn)
    while True:
        if full():
            return 3
        y = random.randint(0, 2)
        x = random.randint(0, 2)
        if tempgrid[y][x] != "X":
            return [y, x]


def full():
    for i in grid:
        for y in i:
            if y == " ":
                return False
    return True


compwin = 0
randomwin = 0
ties = 0

for i in range(1000):
    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    while True:
        while True:
            if full():
                break
            y = random.randint(0, 2)
            x = random.randint(0, 2)
            if grid[y][x] == " ":
                grid[y][x] = "X"
                break

        if full():
            if win("O", grid):
                compwin += 1
                break
            elif win("X", grid):
                randomwin += 1
                break
            elif full():
                ties += 1
                break

        Olis = ai()
        if Olis != 3:
            grid[Olis[0]][Olis[1]] = "O"

        if win("O", grid):
            compwin += 1
            break
        elif win("X", grid):
            randomwin += 1
            break

print("TIES: " + str(ties))
print("RANDOM WINS: " + str(randomwin))
print("COMPUTER WINS: " + str(compwin))
