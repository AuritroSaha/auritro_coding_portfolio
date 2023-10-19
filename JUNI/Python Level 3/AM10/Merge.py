import random

A = []
B = []

for i in range(10):
    A.append(random.randint(1, 100))
    B.append(random.randint(1, 100))

A.sort()
B.sort()

print(A)
print(B)


def merge(a, b):
    merged = []
    index = 0
    while len(a) != 0 and len(b) != 0:
        if a[index] <= b[index]:
            print(2)
            merged.append(a[index])
            a.pop(index)
        elif a[index] >= b[index]:
            print(3)
            merged.append(b[index])
            b.pop(index)

    merged = merged + b
    merged = merged + a

    return merged


print(merge(A, B))