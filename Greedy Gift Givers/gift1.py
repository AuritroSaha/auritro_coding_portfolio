"""
ID: auritro1
LANG: PYTHON3
TASK: gift1
"""

f = open("gift1.in", "r")

values = [x.strip() for x in f.readlines()]

group = {}

for i in range(int(values[0])):
    group[values[i+1]] = 0

currentLineNumber = int(values[0]) + 1

while currentLineNumber < len(values):
    giver = values[currentLineNumber]
    currentLineNumber += 1
    amount, numRecipients = [int(x) for x in values[currentLineNumber].split()]
    currentLineNumber += 1
    group[giver] -= amount
    if numRecipients == 0:
        group[giver] += amount
    else:
        group[giver] += amount%numRecipients
        amount -= amount%numRecipients
        for i in range(numRecipients):
            group[values[currentLineNumber]] += amount/numRecipients
            currentLineNumber += 1

f = open("gift1.out", "w")

for i in group:
    f.write(i+" "+str(int(group[i]))+"\n")
