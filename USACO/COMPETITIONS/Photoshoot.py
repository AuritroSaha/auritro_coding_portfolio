numcows = int(input())
photo = input()
line = []
for i in photo:
    line.append(i)

amounteven = 0
temp = 0

for i in range(numcows):
    if temp == 1:
        temp = 0
        pass
    elif line[i] == "G":
        amounteven += 1
        temp = 1


def flip(lis, x):
    prefix = lis[:x]
    del lis[:x]
    for j in prefix:
        lis.insert(0, j)

    return lis


def evens(lis):
    x = 0

    for h in range(len(lis)):
        if h % 2 != 0 and lis[h] == "G":
            x += 1

    return x


even = 0
reversals = 0

while even != amounteven:
    newline = []
    for i in range(1, numcows + 1):
        even = evens(line)

        line2 = []
        for j in line:
            line2.append(j)

        if evens(flip(line2, i)) > even:
            even = evens(flip(line2, i))
            for k in line2:
                newline.append(k)

    even = 6

    if len(newline) == numcows:
        line.clear()
        reversals += 1
        print(reversals)
        print(even)
        for i in newline:
            line.append(i)

print(reversals)