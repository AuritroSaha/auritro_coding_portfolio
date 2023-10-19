import random, time

num = []
num2 = []
num3 = []

for i in range(100):
    num.append(random.randint(1, 1000))

for i in range(1000):
    num2.append(random.randint(1, 10000))

for i in range(10000):
    num3.append(random.randint(1, 100000))

# num.sort()
# num2.sort()
# num3.sort()


num.sort()
num.reverse()
num2.sort()
num2.reverse()
num3 = sorted(num3, reverse=True)


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


def quicksortnonrandom(lis, pivot):
    if len(lis) == 0:
        return lis

    x = partition(lis, lis[pivot])

    return quicksort(x[0]) + x[1] + quicksort(x[2])


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


print("SORTING TIMING TEST WITH 100 ITEMS\n")
start = time.time()
mergesort(num)
end = time.time()
print("Mergesort: " + str(end - start) + "seconds")
start = time.time()
quicksort(num)
end = time.time()
print("Quicksort: " + str(end - start) + "seconds")
start = time.time()
quicksortnonrandom(num, 0)
end = time.time()
print("Quicksort(nonrandom pivot): " + str(end - start) + "seconds")

print("\nSORTING TIMING TEST WITH 1000 ITEMS\n")
start = time.time()
mergesort(num2)
end = time.time()
print("Mergesort: " + str(end - start) + "seconds")
start = time.time()
quicksort(num2)
end = time.time()
print("Quicksort: " + str(end - start) + "seconds")
start = time.time()
quicksortnonrandom(num2, 0)
end = time.time()
print("Quicksort(nonrandom pivot): " + str(end - start) + "seconds")

print("\nSORTING TIMING TEST WITH 10000 ITEMS\n")
start = time.time()
mergesort(num3)
end = time.time()
print("Mergesort: " + str(end - start) + "seconds")
start = time.time()
quicksort(num3)
end = time.time()
print("Quicksort: " + str(end - start) + "seconds")
start = time.time()
quicksortnonrandom(num3, 0)
end = time.time()
print("Quicksort(nonrandom pivot): " + str(end - start) + "seconds")