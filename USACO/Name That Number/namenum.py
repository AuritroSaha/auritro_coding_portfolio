"""
ID: auritro1
LANG: PYTHON3
TASK: namenum
"""

valids = open("dict.txt", "r")

f = open("namenum.in", "r")

values = [x.strip() for x in valids.readlines()]
serial = f.readline().strip()

conversion = {"A": 2, "B": 2, "C": 2, "D": 3, "E": 3, "F": 3, "G": 4, "H": 4, "I": 4, "J": 5, "K": 5, "L": 5, "M": 6,
              "N": 6, "O": 6, "P": 7, "R": 7, "S": 7, "T": 8, "U": 8, "V": 8, "W": 9, "X": 9, "Y": 9}

names = []

for i in values:
    if len(i) == len(serial):
        temp = ""
        for j in i:
            if j == "Q" or j == "Z":
                break
            temp += str(conversion[j])
        if temp == serial:
            names.append(i)

if len(names) == 0:
    names.append("NONE")

f = open("namenum.out", "w")

for i in names:
    f.write(i + "\n")

f.close()
