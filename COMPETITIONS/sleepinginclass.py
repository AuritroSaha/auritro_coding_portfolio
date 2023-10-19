numcases = int(input())

cases = []
for i in range(numcases):
    n = int(input())
    l = input().split(" ")
    l = [int(i) for i in l]
    cases.append([n, l])


def allequal(lis):
    length = lis[0]
    periods = lis[1]
    maximum = sum(periods)+1
    minimum = max(periods)
    target = 0
    for target in range(minimum, maximum):
        s = 0
        for i in periods:
            s += i
            if s > target:
                s = -1
                break
            elif s == target:
                s = 0
        if s != -1:
            break
    if target == 0:
        return 0
    return length - ((maximum-1)//target)


for i in cases:
    print(allequal(i))
















# numcases = input()
# cases = []
#
# for j in range(int(numcases)):
#     periods = int(input())
#     times = input().strip()
#     time = []
#     for i in times:
#         time.append(int(i))
#     x = [periods, time]
#     cases.append(x)
#
#
# def allequal(numnums, lis, mods):
#     global minvals
#     temp = lis[0]
#     tf = True
#     for i in lis:
#         if i != temp:
#             tf = False
#     if len(lis) == 1 or tf:
#         return mods
#
#     minimum = sum(lis)
#     for i in range(numnums - 1):
#         if lis[i] + lis[i + 1] < minimum:
#             minvals = [i, i + 1]
#             minimum = sum(lis[i] + lis[i + 1])
#
#     lis[minvals[0]] = minimum
#     lis.pop(minvals[1])
#
#     mods += 1
#
#     return allequal(numnums - 1, lis, mods)
#
#
# for i in cases:
#     allequal(i[0], i[1], 0)
