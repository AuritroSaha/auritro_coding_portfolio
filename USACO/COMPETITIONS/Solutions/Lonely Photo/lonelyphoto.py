numcows = int(input())
photo = input()

lonely = 0

for i in range(len(photo)):
    G = 0
    H = 0
    for j in range(i, len(photo)):
        if photo[j] == "G":
            G += 1
        elif photo[j] == "H":
            H += 1
        if (G == 1 or H == 1) and G+H > 2:
            lonely += 1

print(lonely)