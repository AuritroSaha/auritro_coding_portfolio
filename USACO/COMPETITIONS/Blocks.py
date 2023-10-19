from itertools import permutations

numwords = int(input())

blocks = []

for i in range(4):
    lis = input()
    temp = []
    for j in lis:
        temp.append(j)
    blocks.append(temp)

words = []

for i in range(6):
    words.append(input())

for i in words:
    temp = list(permutations(blocks))
    for b in temp:
        alis = []
        for n in b:
            alis.append(n)
        for j in i:
            outBlocks = True
            for a in alis:
                if j in a:
                    alis.remove(a)
                    outBlocks = False
            if outBlocks:
                possible = "NO"
                break
            possible = "YES"
        if possible == "YES":
            break
    print(possible)
