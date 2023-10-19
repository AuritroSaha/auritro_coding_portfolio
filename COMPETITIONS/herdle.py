correct = []
guess = []
for row in range(3):
    x = input().strip()
    correct.append(x)
for row in range(3):
    x = input().strip()
    guess.append(x)


def green(correct1, guess1):
    g = 0
    for i in range(3):
        for j in range(3):
            if correct1[i][j] != "1":
                if correct1[i][j] == guess1[i][j]:
                    correct1[i] = correct1[i].replace(correct1[i][j], "1", 1)
                    guess1[i] = guess1[i].replace(guess1[i][j], "1", 1)
                    g += 1

    return g


def yellow(correct2, guess2):
    y = 0
    for i in range(3):
        for j in range(3):
            if guess2[i][j] != "1":
                for f in range(3):
                    if guess2[i][j] != "1":
                        if guess2[i][j] in correct2[f]:
                            correct2[f] = correct2[f].replace(guess2[i][j], "1", 1)
                            guess2[i] = guess2[i].replace(guess2[i][j], "1", 1)
                            y += 1

    return y


print(green(correct, guess))
print(yellow(correct, guess))
