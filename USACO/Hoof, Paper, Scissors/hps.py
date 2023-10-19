f = open("hps.in", "r")

values = [x.strip() for x in f.readlines()]
values.pop(0)

hps = [{"1": "2", "2": "3", "3": "1"}, {"2": "1", "1": "3", "3": "2"}]

# {"h":"s", "s":"p", "p":"h"}

# {"h":1, "p":2, "s":3}
# {"h":1, "p":3, "s":2}
# {"h":2, "p":1, "s":3}
# {"h":2, "p":3, "s":1}
# {"h":3, "p":1, "s":2}
# {"h":3, "p":2, "s":1}


max = 0
temp = 0

for i in values:
    x,y = i.split()
    if hps[0][x] == y:
        temp += 1

if temp > max:
    max = temp

temp = 0

for i in values:
    x,y = i.split()
    if hps[1][x] == y:
        temp += 1
if temp > max:
    max = temp

f = open("hps.out", "w")

f.write(str(max)+"\n")