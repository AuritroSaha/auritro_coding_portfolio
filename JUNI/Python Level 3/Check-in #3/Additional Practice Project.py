f = open("input.txt", "r")


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


numf = []

for i in f.readlines():
    i = i.strip()
    numf.append(ord(i))

sortednumf = mergesort(numf)

f.close()

f = open("sortedinput.txt", "w")

for i in sortednumf:
    f.write(chr(i) + "\n")

f.close()