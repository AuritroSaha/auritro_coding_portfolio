import random

num = []

for i in range(10):
    num.append(random.randint(1, 100))


def split(lis):
    if len(lis) == 1 or len(lis) == 0:
        print(lis)
        return

    mid = len(lis) // 2

    split(lis[0:mid])
    split(lis[mid:-1])


split(num)