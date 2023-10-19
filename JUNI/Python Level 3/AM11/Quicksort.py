import random

num = []

for i in range(10):
    num.append(random.randint(1, 5))

print(num)


def partition(lis, pivot):
    less = []
    equal = []
    greater = []

    for i in lis:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)

    return less, equal, greater


def quicksort(lis):
    if len(lis) == 0:
        return lis

    pivot = random.randint(0, len(lis) - 1)

    x = partition(lis, lis[pivot])

    return quicksort(x[0]) + x[1] + quicksort(x[2])


print(quicksort(num))

# Best:O(n(log)n)
# Worst: O(n^2)
