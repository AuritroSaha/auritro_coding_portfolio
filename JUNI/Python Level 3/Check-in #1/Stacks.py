# main.py

nums = [1, 2, 3, 4, 5]

nums.append(19)

print(nums)

nums.pop()

print(nums)


# Write a function that takes in a string of key presses and returns the word that the key presses produce. A "#" in the string of key presses represents hitting the backspace button.

# Examples:
# makeWord("hi#") -> "h"
# makeWord("ok##") -> ""
# makeWord("ti#ger") -> "tger"
# makeWord("t###") -> ""

def makeWord(x):
    word = []
    finalword = ""

    for i in x:
        if i == "#":
            if len(word) >= 1:
                word.pop()
        else:
            word.append(i)

    for i in word:
        finalword += i

    return finalword


print(makeWord("hi#####peop#le"))


