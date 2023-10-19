import random


def selectionsort(lis):
    lislen = len(lis)
    nlis = []
    for j in range(lislen):
        lowest = lis[0]
        for i in lis:
            if i < lowest:
                lowest = i
        lis.remove(lowest)
        nlis.append(lowest)
    return nlis


num = []

for i in range(10):
    num.append(random.randint(0, 100))

print(num)


# print(selectionsort(num))

# n + (n-1) + (n-2) + ...
# 6 + 5 + 4 + 3 + 2 + 1
# n(n+1)/2
# Time complexity: O(n^2)
# Space complexity: O(n)


# Homework: Write the selection sort algorithm to use O(1) space instead of O(n) space

def selectionsort2(lis):
    lislen = len(lis)
    for j in range(lislen):
        lowest = j
        for i in range(j, lislen):
            if lis[i] < lis[lowest]:
                lowest = i
        temp = lis[lowest]
        lis[lowest] = lis[j]
        lis[j] = temp
    return lis


print(selectionsort2(num))

# Homework: Record a video or just audio of you describing the selection sort algorithm and explain the difference between the two versions you wrote 