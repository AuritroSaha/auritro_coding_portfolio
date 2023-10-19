numcows = int(input())
order = str(input())

lonely = 0

for i in range(len(order)-2):
    for j in range(i+3, len(order)+1):
        photo = order[i:j]
        G = 0
        H = 0
        for p in photo:
            if p == "G" or p == "g":
                G += 1
            elif p == "H" or "h":
                H += 1
        if G == 1 or H == 1:
            lonely += 1

print(lonely)