f = open("notlast.in", "r")

values = [x.strip().split() for x in f.readlines()]
values.pop(0)

milks = {"Bessie":0, "Elsie":0, "Daisy":0, "Gertie":0, "Annabelle":0, "Maggie":0, "Henrietta":0}

for i in values:
    milks[i[0]] += int(i[1])

sorted_times = sorted(list(milks.values()))

temp = min(sorted_times)
second = temp

for i in sorted_times:
    if i != temp:
        second = i
        break

name = ""
temp = 0

for i in milks:
    if milks[i] == second:
        temp += 1
        name = i

f = open("notlast.out", "w")

if temp > 1:
    f.write("Tie\n")
else:
    f.write(name+"\n")
