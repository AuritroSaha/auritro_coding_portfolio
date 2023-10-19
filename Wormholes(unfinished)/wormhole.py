"""
ID: roobeel1
LANG: PYTHON3
TASK: wormhole
"""
import itertools

f = open("wormhole.in", "r")

points = [x.strip().split() for x in f.readlines()]
numports = int(points[0][0])//2
points.remove(points[0])

x = []
y = []
p = []

for i in points:
    x.append(int(i[0]))
    y.append(int(i[1]))

for i in range(len(x)):
    p.append(i)

pairings = list(itertools.combinations(p, 2))
pairings = list(itertools.combinations(pairings, numports))
finalpairings = []
pairings = set(pairings)

for i in pairings:
    # fix later more than 2 pairs of ports
    temp = 0
    smain = set()
    for j in i:
        smain.add(j[0])
        smain.add(j[1])
        temp += 2

    if len(smain) == temp:
        finalpairings.append(i)
        # print(i)
        # print(smain)
#
print(finalpairings)


def closesthole(current):
    for i in p:
        if x[current] < x[i] and y[current] == y[i]:
            return i
    return -1


loops = 0

for pair in finalpairings:
    partners = {}
    for i in pair:
        partners[i[0]] = i[1]
        partners[i[1]] = i[0]
    #print(partners)
    for start in p:
        pos = start
        for i in range(len(p)):
            pos = partners[pos]
            pos = closesthole(pos)
            if pos == -1:
                break
        if pos != -1:
            loops += 1
            print(start)
            print(partners)
            break

f = open("wormhole.out", "w")

f.write(str(loops) + "\n")
