def insertionsort(lis):
    lenlis = len(lis)
    nlis = []
    for i in range(lenlis):
        nlis.append(lis[0])
        lis.pop(0)
        index = -1
        if len(nlis) == 1:
            pass
        else:
            while True:
                if -(len(nlis)) == index:
                    break
                elif nlis[index] <= nlis[index - 1]:
                    temp = nlis[index]
                    nlis[index] = nlis[index - 1]
                    nlis[index - 1] = temp
                    index = index - 1
                elif nlis[index] > nlis[index - 1]:
                    break
    return nlis


num = [17, 1, 4, 6, 2, 19, 50, 3, 7, 5]

print(insertionsort(num))

num = [17, 1, 4, 6, 2, 19, 50, 3, 7, 5]


def insertionsort2(lis):
    lenlis = len(lis)
    for i in range(lenlis):
        num = lis[i]
        index = i
        while True:
            if 0 == index:
                break
            elif lis[index] <= lis[index - 1]:
                temp = lis[index]
                lis[index] = lis[index - 1]
                lis[index - 1] = temp
                index = index - 1
            elif lis[index] > lis[index - 1]:
                break
    return lis


print(insertionsort2(num))