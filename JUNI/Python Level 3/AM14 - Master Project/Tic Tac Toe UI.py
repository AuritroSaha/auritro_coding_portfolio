import random

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def printgrid(grid):
    print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
    print("---+---+---")
    print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
    print("---+---+---")
    print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])


printgrid(grid)

winner = ""


def win(key):
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


def full():
    for i in grid:
        for y in i:
            if y == " ":
                return False
    return True


while True:
    print()
    user = input("Give the coordinates that you want to make yours(ex: 1,3): ")
    print()
    user = user.replace(",", "")
    grid[int(user[1]) - 1][int(user[0]) - 1] = "X"

    while True:
        if full():
            break
        y = random.randint(0, 2)
        x = random.randint(0, 2)
        if grid[y][x] == " ":
            grid[y][x] = "O"
            break

    printgrid(grid)

    if win("O"):
        print("You Lost.")
        break
    elif win("X"):
        print("You Won!")
        break
    elif full():
        print("It's a tie.")
        break