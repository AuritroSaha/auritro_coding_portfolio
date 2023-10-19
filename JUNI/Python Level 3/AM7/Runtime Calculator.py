# main.py

import time, random

num = []

for i in range(1000000):
    num.append(random.randint(0, 100000))


def binarysearchit(n, lis):
    while (len(lis) > 0):
        if lis[len(lis) // 2] == n:
            return True
        if len(lis) == 1:
            break
        elif lis[len(lis) // 2] > n:
            lis = lis[:len(lis) // 2]
        else:
            lis = lis[len(lis) // 2:]

    return False


def linearsearch(lis, num):
    for i in lis:
        if num == i:
            return True
    return False


linstart = time.time()

for i in range(1000):
    linearsearch(num, random.randint(0, 100000))
linend = time.time()
lintime = linend - linstart

num.sort()

bistart = time.time()

for i in range(1000):
    binarysearchit(random.randint(0, 100000), num)
biend = time.time()
bitime = biend - bistart

print("Linear search took " + str(lintime) + " seconds")
print("Binary search took " + str(bitime) + " seconds")