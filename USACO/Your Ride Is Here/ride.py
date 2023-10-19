"""
ID: auritro1
LANG: PYTHON3
TASK: ride
"""

# alpha = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
#          "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
#          "Z": 26}



def convert(lis):
    new = []
    for i in lis:
        new.append(ord(i)-64)

    total = 1

    for i in new:
        total = total * i

    return total % 47


f = open("ride.in", "r")

info = f.readlines()

comet = convert(info[0].strip())
group = convert(info[1].strip())

f.close()

f = open("ride.out", "w")

if comet == group:
    f.write("GO\n")
else:
    f.write("STAY\n")
