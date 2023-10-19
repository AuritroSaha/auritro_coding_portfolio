# main.py

# HW: Brainstorm potential algorithms using a stack for this problem

# ([])}

# "([{}]{)}"

def parval(x):
    parentheses = {")": "(", "]": "[", "}": "{"}
    parStack = []
    for i in x:
        if i == "(" or i == "{" or i == "[":
            parStack.append(i)
        elif i == ")" or i == "}" or i == "]":
            if len(parStack) <= 0:
                return False
            if parentheses[i] != parStack.pop():
                return False
    if len(parStack) > 0:
        return False
    return True


print(parval("{()[]}"))
print(parval("{(((())))[}]"))


def recparval(x):
    parentheses = {")": "(", "]": "[", "}": "{"}
    if len(x) == 0:
        return True
    for i in range(len(x)):
        if x[i] == ")" or x[i] == "}" or x[i] == "]":
            if parentheses[x[i]] != x[i - 1]:
                return False
            x = x[:i - 1] + x[i + 1:]
            return recparval(x)


print(recparval("{()[]}"))
print(recparval("{(((())))[}]"))