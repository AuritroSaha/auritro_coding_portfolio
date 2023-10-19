stalls = int(input())
p = input().split()
t = input().split()
p = [int(x) for x in p]
t = [int(x) for x in t]

diffs = []
for i in range(len(t)):
    diffs.append(p[i] - t[i])

moves = 0

while len(diffs) != 0:
    if diffs[0] == 0:
        diffs.remove(diffs[0])
    else:
        if diffs[0] > 0:
            temp = []
            for i in range(len(diffs)):
                if diffs[i] > 0:
                    temp.append(diffs[i])
                else:
                    break
            tmin = min(temp)
            for i in range(len(temp)):
                diffs[i] = diffs[i] - tmin
            moves += tmin

        elif diffs[0] < 0:
            temp = []
            for i in range(len(diffs)):
                if diffs[i] < 0:
                    temp.append(diffs[i])
                else:
                    break
            tmin = max(temp)
            for i in range(len(temp)):
                diffs[i] = diffs[i] - tmin
            moves -= tmin

print(moves)

# changes = 0
#
# while True:
#     diffs = []
#     for i in range(len(t)):
#         diffs.append(p[i] - t[i])
#
#     diff = 0
#
#     while True:
#         temp = 0
#         for i in range(len(diffs)):
#             if diffs[i] == 0:
#                 if t[i] != t[0] or t[i] != t[-1]:
#                     diff = 1
#                 diffs.remove(diffs[i])
#                 t.remove(t[i])
#                 p.remove(p[i])
#                 temp += 0
#                 break
#         if temp == 0:
#             break
#
#     if len(diffs) == 0:
#         break
#
#     tmin = min(diffs)
#
#     if diff == 0:
#         for i in range(len(t)):
#             t[i] += tmin
#         changes += tmin
#     elif diff == 1:
#         for i in range(len(t)):
#             t[i] += tmin
#             changes += tmin
#
# print(changes)
