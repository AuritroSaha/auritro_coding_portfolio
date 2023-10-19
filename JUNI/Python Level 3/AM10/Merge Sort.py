# main.py

# Use merge() from earlier to complete this
# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/

import random

A = []
B = []

for i in range(10):
    A.append(random.randint(1, 100))
    B.append(random.randint(1, 100))

print("Unsorted: " + str(A))


def merge(a, b):
    merged = []
    index = 0
    while len(a) != 0 and len(b) != 0:
        if a[index] <= b[index]:
            merged.append(a[index])
            a.pop(index)
        elif a[index] >= b[index]:
            merged.append(b[index])
            b.pop(index)

    merged = merged + b
    merged = merged + a

    return merged


def mergesort(lis):
    mid = len(lis) // 2
    if len(lis) == 1:
        return lis

    return merge(mergesort(lis[mid:]), mergesort(lis[:mid]))


print("Sorted: " + str(mergesort(A)))

# O(n(log(n)))



