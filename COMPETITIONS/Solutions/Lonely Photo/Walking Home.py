cases = []
turns = []

numcases = int(input().strip())
for i in range(numcases):
    dim, turns0 = input().strip().split()
    dim = int(dim)
    turns0 = int(turns0)
    turns.append(turns0)
    cases.append([])
    for j in range(dim):
        cases[i].append(input())


def turns1(lis):
    routes = 0
    temp = 0
    if "H" not in lis[0]:
        for i in lis:
            if i[-1] != "H":
                temp += 1
    if temp == len(lis):
        routes += 1

    temp = 0
    if "H" not in lis[-1]:
        for i in lis:
            if i[0] != "H":
                temp += 1
    if temp == len(lis):
        routes += 1

    return routes

def turns2(lis):
    routes = 0
    #DRD
    # Pick a row
    for d in range(1,len(lis)-1):
        count = 3
        # Check all spaces above the row and in column 0
        for i in range(1,d):
            if lis[i][0] == "H":
                count -= 1
                break
        # Check the row itself
        if lis[d].count("H") != 0:
            count -= 1
        # Check all spaces below the row and in the last column
        for i in range(d,len(lis)):
            if lis[i][-1] == "H":
                count -= 1
                break
        if count == 3:
            routes += 1
    #
    # RDR
    for d in range(1,len(lis)-1):
        count = 3
        # Check all spaces to the left of d and in row 0
        for i in range(1,d):
            if lis[0][i] == "H":
                count -= 1
                break
        # Check the column itself
        for i in range(1,d):
            if lis[i][d] == "H":
                count -= 1
        # Check all spaces to the right of the column
        for i in range(d,len(lis)):
            if lis[-1][i] == "H":
                count -= 1
                break
        if count == 3:
            routes += 1

    return routes + turns1(lis)



    #RDR