"""
ID: auritro1
LANG: PYTHON3
TASK: milk
"""

f = open("milk.in", "r")

values = [x.strip().split() for x in f.readlines()]

units = int(values[0][0])

valdict = {}

for i in values:
    if int(i[0]) in valdict:
        valdict[int(i[0])] += int(i[1])
    else:
        valdict[int(i[0])] = int(i[1])


total = 0

del valdict[units]

while units > 0:
    tmin = -1

    for i in valdict:
        if tmin == -1:
            tmin = i
        elif i < tmin:
            tmin = i

    if valdict[tmin] >= units:
        global amount
        amount = units
    else:
        amount = valdict[tmin]

    units -= amount
    valdict[tmin] -= amount
    total += tmin * amount
    print("Price", tmin)
    print("Amount", amount)
    print("Total", total)
    print("Units", units)
    if valdict[tmin] == 0:
        del valdict[tmin]

f = open("milk.out", "w")

f.write((str(total)) + "\n")
