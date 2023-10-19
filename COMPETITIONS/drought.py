numcases = int(input())

cases = []

for i in range(numcases):
    cases.append([])
    cases[i].append(int(input()))
    cases[i].append([int(f) for f in input().split()])

# differences between adjacent nums added up times 2 is amount needed?
# check for impossible by checking that the max diff between any 2 adjacent nums is at most 1?

for i in cases:
    if len(set(i[1])) == 1:
        print(0)
        break
    if len(set(i[1])) != 1 and 0 in i[1]:
        print(-1)
        break
    corn = 0
    s = sorted(i[1])
    min1 = int(s[0])
    min2 = int(s[1])
    g = min2 - min1
    for j in range(len(i[1])-1):
        if int(i[1][j]) < 1:
            print(-1)
            break
        i[1][j] -= i[1][j] - g
        i[1][j+1] -= i[1][j] - g
        corn += 2*(i[1][j] - g)

    print(corn)
    if len(set(i[1])) == 1:
        print(corn)
    else:
        print(-1)

print(cases)