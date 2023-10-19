numpapers, citations = input().split()

numpapers = int(numpapers)
citations = int(citations)

papers = input().split()
papers = [int(x) for x in papers]
papers.sort(reverse=True)


# given the lis tof numbers in descending order we want to return the maximum h-value
def hindex(lis):
    for i in range(len(lis), -1, -1):
        if i <= lis[i - 1]:
            return i
    return i


# call hindex on the original list, ignore the first h amount of values in the list, for all vals h + 1 add 1 to each until citations is 0, call hindex again and print highest h

h = hindex(papers)
print(h)
for i in range(h, numpapers):
    if citations == 0:
        break
    papers[i] += 1
    citations -= 1

print(citations)

papers.sort(reverse=True)
print(papers)
print(hindex(papers))