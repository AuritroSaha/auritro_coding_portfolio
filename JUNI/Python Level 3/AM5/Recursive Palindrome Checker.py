# main.py

# racecar" -> "aceca" -> "cec" - "e"

def palcheck(x):
    if len(x) == 1 or len(x) == 0:
        return True
    if x[0] != x[-1]:
        return False
    return palcheck(x[1:-1])


x = input("Enter the string you would like to check.\nWe will check if it is a palindrome.\n")

print(palcheck(x))