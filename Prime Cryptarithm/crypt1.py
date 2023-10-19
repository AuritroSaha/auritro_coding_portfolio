"""
ID: roobeel1
LANG: PYTHON3
TASK: crypt1
"""

f = open("crypt1.in", "r")

digits = f.readlines()[1].split()

solutions = 0

print(digits)

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                for e in digits:
                    if len(str(int(a + b + c) * int(d))) == 3 and len(str(int(a + b + c) * int(e))) == 3:
                        temp = 0
                        for i in str(int(a + b + c) * int(d)):
                            if i not in digits:
                                temp += 1
                                break
                        for i in str(int(a + b + c) * int(e)):
                            if i not in digits:
                                temp += 1
                                break
                        for i in str(int(a + b + c) * int(d + e)):
                            if i not in digits:
                                temp += 1
                                break
                        if temp == 0 and len(str(int(a + b + c) * int(d + e))) == 4:
                            solutions += 1

f = open("crypt1.out", "w")
f.write(str(solutions) + "\n")
