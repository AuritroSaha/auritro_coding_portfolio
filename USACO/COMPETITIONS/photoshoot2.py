numcows = int(input())

original = input()
modded = input()

moves = 0

if original == modded:
    print(moves)
else:
    for i in range(numcows):
        if original[i] != modded[i]:
            for j in range(numcows):
                if modded[j] == original[i]:
                    if j < i:
                        moves += 1
                        modded.insert(i, modded[j])
