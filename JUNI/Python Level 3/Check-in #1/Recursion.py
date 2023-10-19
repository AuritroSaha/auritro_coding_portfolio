# What will be printed if we call strangeFunction(4)?
def strangeFunction(n):
    print(n)
    if n > 2:
        strangeFunction(n - 1)
        strangeFunction(n - 2)


# Once you have an answer, uncomment the next line to test if it is correct!
strangeFunction(4)


# Write a recursive function that takes in a number of rows of a pyramid and returns the number of bowling pins needed to make a pyramid with that number of rows.
def bowlingpins(x, p):
    if x == 1:
        p += 1
        return p

    p += x
    x -= 1

    return bowlingpins(x, p)


# bp(3) = b(2) + 3 = bp(1) + 2 + 3 = 1 + 2 + 3

print(bowlingpins(5, 0))


# Write a recursive function to calculate the nth Lucas number. The Lucas numbers are very similar to the Fibonacci numbers, because each Lucas number is the sum of the previous two numbers. The only difference is that the Lucas number sequence starts with 2, 1 instead of 0, 1. The first few Lucas numbers are: 2, 1, 3, 4, 7, 11

def lucas(x):
    if x == 1:
        return 2
    if x == 2:
        return 1

    return lucas(x - 1) + lucas(x - 2)


print(lucas(7))
