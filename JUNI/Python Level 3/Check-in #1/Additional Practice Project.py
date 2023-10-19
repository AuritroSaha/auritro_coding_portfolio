# main.py

x = [4, 5, 2]  # -> 4 9 11

# Remember: can also slice a list just like with strings
# Another thing: head recusrions vs. tail recursion (order of the base case and recursive call)
# Look at Recursive Cascade for help

num = []


def lisadder(x):
    if len(x) != 1:
        lisadder(x[:-1])
    if len(x) == 1:
        print(x[0])
        return
    print(sum(x))


lisadder(x)

print("-------------------------------------------------")


def lisadder2(x):
    if len(x) == 1:
        print(x[0])
        return
    print(sum(x))
    lisadder2(x[:-1])


lisadder2(x)