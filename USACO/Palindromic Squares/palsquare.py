"""
ID: roobeel1
LANG: PYTHON3
TASK: palsquare
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


f = open("palsquare.in", "r")

base = int(f.readline().strip())

f.close()

f = open("palsquare.out", "w")

for i in range(1, 301):
    squared = i ** 2

    coned = convert_to_base(squared, base)

    if coned == coned[::-1]:
        f.write(convert_to_base(i, base) + " " + coned + "\n")
