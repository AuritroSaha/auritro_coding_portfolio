"""
ID: auritro1
LANG: PYTHON3
TASK: beads
"""

f = open("beads.in", "r")

values = f.readlines()

necklace = values[1] * 2
print(necklace)

tempMax = 0
maximum = 0

for i in range(int(values[0].strip())):
    i = i - 1
    currentColor = necklace[i]

    isWhite = True if currentColor == "w" else False

    diffColors = 0

    while diffColors < 2:

        if necklace[i] == currentColor:
            tempMax += 1
        elif necklace[i] == "w":
            tempMax += 1
        else:
            if isWhite:
                isWhite = False
            else:
                diffColors += 1
                if diffColors == 2:
                    break
            currentColor = necklace[i]
            tempMax += 1
        i += 1

    if tempMax > maximum:
        maximum = tempMax
    tempMax = 0

f = open("beads.out", "w")

f.write(str(maximum) + "\n")
