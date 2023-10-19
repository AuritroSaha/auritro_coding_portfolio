staircaselist = []

temp = 1


def test():
    if temp == 1:
        print("yes")


def staircase(x, temp):
    if temp == 1:
        staircaselist.append(x)
        temp = temp - 1
    if len(x) == 1:
        return x
    staircaselist.append(x[:-1])
    return staircase(x[:-1], temp)


staircase("dog", 1)

for i in range(len(staircaselist) - 1, -1, -1):
    print(staircaselist[i])

for i in range(len(staircaselist)):
    print(staircaselist[i])

print("----------------------")


# Another way
def cascade(word):
    if len(word) > 1:
        cascade(word[:-1])
    print(word)


def inverse_cascade(word):
    print(word)
    if len(word) > 1:
        inverse_cascade(word[:-1])


cascade("dog")
inverse_cascade("dog")