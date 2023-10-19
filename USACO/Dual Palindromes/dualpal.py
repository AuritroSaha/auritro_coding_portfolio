"""
ID: roobeel1
LANG: PYTHON3
TASK: dualpal
"""

def convert_to_base(num, conbase):
    conum = ""

    power = 0
    while num >= conbase ** power:
        power += 1

    power -= 1

    numconvert = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J"}

    for i in range(power, -1, -1):
        if num // conbase ** i < 10:
            conum += str(num // conbase ** i)
        else:
            conum += numconvert[num // conbase ** i]

        num = num % conbase ** i

    return conum

f = open("dualpal.in", "r")

pals, start = [int(x) for x in f.readline().split()]

f.close()

f = open("dualpal.out", "w")

start += 1

temp = 0

while temp < pals:
    temp1 = 0
    for i in range(2,11):
        coned = convert_to_base(start, i)
        if coned == coned[::-1]:
            temp1 += 1
            if temp1 == 2:
                f.write(str(start)+"\n")
                temp += 1
                break

    start += 1