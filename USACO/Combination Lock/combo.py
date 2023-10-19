"""
ID: roobeel1
LANG: PYTHON3
TASK: combo
"""

f = open("combo.in", "r")

dial = f.readline()
farmer_key = [int(x) for x in f.readline().split()]
master_key = [int(x) for x in f.readline().split()]

dial_range = []
farmer_range = []
master_range = []

for i in range(1, int(dial) + 1):
    dial_range.append(i)

if int(dial) >= 5:
    for i in farmer_key:
        farmer_range.append([dial_range[i - 3], dial_range[i - 2], dial_range[i - 1], dial_range[i % int(dial)], dial_range[(i + 1) % int(dial)]])
    for i in master_key:
        master_range.append([dial_range[i - 3], dial_range[i - 2], dial_range[i - 1], dial_range[i % int(dial)], dial_range[(i + 1) % int(dial)]])

    combos = set()

    for a in farmer_range[0]:
        for b in farmer_range[1]:
            for c in farmer_range[2]:
                combos.add(str([a, b, c]))

    for a in master_range[0]:
        for b in master_range[1]:
            for c in master_range[2]:
                combos.add(str([a, b, c]))

    print(dial_range)
    print(farmer_range)
    print(master_range)

    f = open("combo.out", "w")
    f.write(str(len(combos)) + "\n")

else:
    farmer_range = [[], [], []]
    master_range = [[], [], []]

    for j in range(3):
        for i in range(len(dial_range)):
            farmer_range[j].append(i + 1)
            master_range[j].append(i + 1)

    combos = set()

    for a in farmer_range[0]:
        for b in farmer_range[1]:
            for c in farmer_range[2]:
                combos.add(str([a, b, c]))

    for a in master_range[0]:
        for b in master_range[1]:
            for c in master_range[2]:
                combos.add(str([a, b, c]))

    print(dial_range)
    print(farmer_range)
    print(master_range)

    f = open("combo.out", "w")
    f.write(str(len(combos)) + "\n")

f.close()
