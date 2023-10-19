numcases = int(input())


def beats(d1, d2):
    d1w = 0
    d2w = 0
    for i1 in d1:
        for j in d2:
            if i1 > j:
                d1w += 1
            elif j > i1:
                d2w += 1

    return d1w > d2w


def ifTransitive(e, f):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for a in nums:
        for b in nums:
            for c in nums:
                for d in nums:
                    trial = [a, b, c, d]
                    if beats(e, f) and beats(f, trial) and beats(trial, e):
                        print("yes")
                        return 0
                    elif beats(f, e) and beats(trial, f) and beats(e, trial):
                        print("yes")
                        return 0
                    # if beats(beats(i[0], i[1]), trial) == trial:
                    #     if beats(i[0], i[1]) == i[0]:
                    #         if beats(i[1], trial) == i[1]:
                    #             yes = True
                    #     else:
                    #         if beats(i[0], trial) == i[0]:
                    #             yes = True
    print("no")
    return 0


for n in range(numcases):
    d = input().split(" ")
    s1 = d[:4]
    s1 = [int(i) for i in s1]
    s2 = d[4:]
    s2 = [int(i) for i in s2]
    ifTransitive(s1, s2)
