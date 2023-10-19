f = open("square.in", "r")

lines = f.readlines()

temp = []

x = []
y = []

for i in lines:
    temp.append(i.split())

for i in temp:
    for j in range(len(i)):
        if j % 2 == 0:
            x.append(int(i[j]))
        else:
            y.append(int(i[j]))

xdistance = max(x)-min(x)
ydistance = max(y)-min(y)

f.close()

f = open("square.out", "w")

if xdistance >= ydistance:
    f.write(str(xdistance**2))
else:
    f.write(str(ydistance**2))



