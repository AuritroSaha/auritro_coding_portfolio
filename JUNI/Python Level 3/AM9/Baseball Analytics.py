import copy

# List of baseball players with random stats
p1 = ["B. Harper", .254, 27, 92]
p2 = ["J. Soler", .256, 36, 91]
p3 = ["C. Yelich", .329, 41, 89]
p4 = ["C. Bellinger", .312, 42, 100]
p5 = ["M. Trout", .299, 41, 99]
p6 = ["F. Lindor", .296, 23, 56]
p7 = ["M. Betts", .285, 21, 67]
p8 = ["A. Rendon", .328, 29, 104]
p9 = ["D. Lemahieu", .331, 22, 87]
p10 = ["R. Acuna", .290, 36, 89]

playerList = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


def baseballsort(lis, index, leaderboard):
    nlis = copy.deepcopy(lis)
    for i in range(len(nlis), 0, -1):
        for j in range(i - 1):
            if nlis[j][index] < nlis[j + 1][index]:
                temp = nlis[j]
                nlis[j] = nlis[j + 1]
                nlis[j + 1] = temp

    print(leaderboard + " Leaderboard: ")

    for i in nlis:
        print("   " + i[0])


baseballsort(playerList, 1, "Average")
baseballsort(playerList, 2, "Home Run")
baseballsort(playerList, 3, "RBI")