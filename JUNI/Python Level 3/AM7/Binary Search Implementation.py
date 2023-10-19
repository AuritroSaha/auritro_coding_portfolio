import random

num = []

for i in range(20):
    num.append(random.randint(1, 50))

num.sort()

print(num)


# Actual runtime: O(nlog(n))
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


print(binarysearchit(7, num))


# O(logn)
# 2 ^ i = n

def binarysearchre(n, lis):
    if lis[len(lis) // 2] == n:
        return True
    elif len(lis) <= 1:
        return False

    elif lis[len(lis) // 2] > n:
        lis = lis[:len(lis) // 2]
    else:
        lis = lis[len(lis) // 2:]

    return binarysearchre(n, lis)


print(binarysearchre(7, num))