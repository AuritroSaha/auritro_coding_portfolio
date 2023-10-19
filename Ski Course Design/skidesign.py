"""
ID: roobeel1
LANG: PYTHON3
TASK: skidesign
"""

f = open("skidesign.in", "r")

heights = [int(x) for x in f.readlines()]

heights.remove(heights[0])

price = float("inf")

heights.sort()

# while True:
#     x = max(heights) - min(heights)
#     if x > 17:
#         diff = (x - 17) / 2
#         diff2 = (x - 17) / 2
#         if (x - 17) % 2 != 0:
#             diff = int(diff)
#             diff2 = int(diff2) + 1
#         a = max(heights) - diff
#         b = min(heights) + diff2
#         heights.remove(max(heights))
#         heights.append(a)
#         heights.remove(min(heights))
#         heights.append(b)
#         price += (diff * diff2) * 2
#     else:
#         break

minh = heights[0]
maxh = minh+17
heightsc = heights[:]

while heights[-1] > minh+17:
    cost = 0
    for i in heights:
        if i > maxh:
            cost += (i-maxh)**2
        elif i < minh:
            cost += (i-minh)**2

    if cost < price:
        price = cost
    minh += 1
    maxh += 1

if price == float("inf"):
    price = 0

f = open("skidesign.out", "w")

f.write(str(int(price)) + "\n")
f.close()
