"""
ID: auritro1
LANG: PYTHON3
TASK: friday
"""

year = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
        "September": 30, "October": 31, "November": 30, "December": 31, "Leap": 29}

totals = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

f = open("friday.in", "r")

start = "Monday"

for i in range(int(f.readline())):
    while True:
        if week[0] != start:
            x = week.pop(0)
            week.append(x)
        else:
            break
    i = 1900 + i
    month = "January"
    days = 0
    leap = False
    y = 365
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 == 0:
            leap = True
        elif i % 100 != 0:
            leap = True
    if leap:
        y = 366
    for j in range(y):
        j = j + 1
        days += 1
        if days == 13:
            totals[week[(j % 7)-1]] += 1
        if year[month] == 31:
            if days == 31:
                x = months.index(month)
                if month != "December":
                    month = months[x + 1]
                else:
                    month = "January"
                days = 0
        elif year[month] == 30:
            if days == 30:
                x = months.index(month)
                month = months[x + 1]
                days = 0
        elif year[month] == 28:
            if days == 28:
                month = "March"
                days = 0
        elif year[month] == 29:
            if days == 29:
                month = "March"
                days = 0
        if leap and month == "February":
            month = "Leap"
        if j == y:
            start = week[((y+1) % 7)-1]

f = open("friday.out", "w")

f.write(str(totals["Saturday"])+" "+str(totals["Sunday"])+" "+str(totals["Monday"])+" "+str(totals["Tuesday"])+" "+str(totals["Wednesday"])+" "+str(totals["Thursday"])+" "+str(totals["Friday"])+"\n")

