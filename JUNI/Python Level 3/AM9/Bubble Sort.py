import random


def bubblesort(lis):
    for i in range(len(lis), 0, -1):
        for i in range(i - 1):
            if lis[i] > lis[i + 1]:
                temp = lis[i]
                lis[i] = lis[i + 1]
                lis[i + 1] = temp

    return lis


num = []

for i in range(10):
    num.append(random.randint(0, 100))

print(num)

print(bubblesort(num))

# TIME: O(n^2)

# SPACE: O(n)