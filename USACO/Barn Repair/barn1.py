"""
ID: roobeel1
LANG: PYTHON3
TASK: barn1
"""

f = open("barn1.in", "r")

amounts = f.readline().strip().split()

stalls = [int(x.strip()) for x in f.readlines()]
amounts = [int(x) for x in amounts]

stalls = sorted(stalls)

if amounts[0] > amounts[2]:
    f = open("barn1.out", "w")
    f.write(str(amounts[2])+"\n")
else:
    f = open("barn1.in", "r")

    gaps = []

    for i in range(amounts[2]-1):
        gaps.append(stalls[i+1]-stalls[i]-1)
    gaps.append(0)

    sortgaps = sorted(gaps)

    if amounts[0] == 1:
        x = 0
    else:
        x = len(gaps)

    max = sortgaps[-amounts[0]+1:x]

    boards = 0

    print(stalls)
    print(gaps)
    print(max)

    start = stalls[0]
    for i in range(len(gaps)):
        if gaps[i] in max:
            max.remove(gaps[i])
            boards += (stalls[i]-start)+1
            start = stalls[i+1]
        elif stalls[i] == stalls[-1]:
            boards += (stalls[-1]-start)+1

    f = open("barn1.out", "w")
    f.write(str(boards)+"\n")
