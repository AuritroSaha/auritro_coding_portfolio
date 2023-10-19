movies = {"Endgame": 2019, "Homecoming": 2017, "Black Panther": 2018}

print(movies["Endgame"])

movies["Far From Home"] = 2019
print(movies)

for i in movies:
    print(movies[i])

for i in movies:
    print(i)

if "Infinity War" in movies:
    print("Infinity War is in movies")
else:
    print("Infinity War is not in movies")
    movies["Infinity War"] = 2018

print(movies)

import random

num = {}

for i in range(15):
    x = random.randint(1, 1000)
    num[x] = len(str(x))

print(num)