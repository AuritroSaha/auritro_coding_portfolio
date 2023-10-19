# main.py

'''

# Create empty set
x = set()
x.add(3)
x.add(5)
x.add(7)
x.add(3) # can't add multiple of same element

# for i in range(): DOESN'T WORK

# Iterating through set
for number in x:
  print(number)

# Removing element from set
print(x)
x.remove(5)
print()
print("Set x:")
print(x)
print()

# Intersection and union

y = set([1, 2, 3])
print('Set y:')
print(y)
print()

print(x.intersection(y))
print(x.union(y))

'''

import random

x = set()
y = set()
for i in range(5):
    x.add(random.randint(1, 10))
for i in range(5):
    y.add(random.randint(1, 10))

print(x)
print(y)
print(x.union(y))
print(x.intersection(y))

if 1 in y:
    print("The number 1 is in the second set.")
else:
    print("The number 1 is not in the second set.")

z = input("Give a word: ")

zset = set()

for i in z:
    zset.add(i)

print(zset)
print("There are " + str(len(zset)) + " unique letters in " + z)

q = input("Give another word: ")

qset = set()

for i in q:
    qset.add(i)

print(zset.intersection(qset))


def evenSet():
    nums = set()

    while True:
        num = input("Give a number to put into the set and type stop if you want to stop: ")
        if num == "stop":
            break
        nums.add(int(num))

    temp = []

    for i in nums:
        if i % 2 == 1:
            temp.append(i)

    for i in temp:
        nums.remove(i)

    print(nums)


evenSet()


def threeLetterSet():
    words = set()

    while True:
        word = input("Give a word to put into the set and type stop if you want to stop: ")
        if word == "stop":
            break
        words.add(word)

    temp = []

    for i in words:
        if len(i) != 3:
            temp.append(i)

    for i in temp:
        words.remove(i)

    print(words)


threeLetterSet()








