"""
Sum each digit of the card number, but multiply every other digit by 2, starting at first digit. If the sum is a multiple of 10, credit card is valid!

6  4  7  2  0  1  3  1
12 4  14 2  0  1  6  1 -> 40 -> VALID

1 2 3 4 5 6 7 8 -> INVALID

8 4 6 4 2 1 7 5 -> 60 -> VALID

9 2 4 7 1 8 0 3 -> INVALID

"""

while True:
    crenum = input("Give your credit card number, write STOP if you are done: ")

    if crenum == ("STOP"):
        break

    crelen = len(crenum)

    crenum2 = 0

    for i in range(crelen):
        num = int(crenum[i])
        if i % 2 == 0:
            num = num * 2
        crenum2 = crenum2 + num

    if crenum2 % 10 == 0:
        print("VALID")
    else:
        print("INVALID")

