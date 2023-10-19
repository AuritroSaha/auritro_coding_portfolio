"""
ID: auritro1
LANG: PYTHON3
TASK: milk2
"""


f = open("milk2.in", "r")

values = [x.strip() for x in f.readlines()]

maxMilking = 0
maxInterval = 0

times = {}
times1 = {}

for i in range(len(values)):
    if i != 0:
        start, end = [int(x) for x in values[i].split()]
        if start in times:
            times[start] += 1
        else:
            times[start] = 1
        if end in times:
            times[end] += -1
        else:
            times[end] = -1

temp = sorted(times)

for i in temp:
    times1[i] = times[i]

start = 0
end = 0
interval = 0
if0 = 0
lastInterval = 0
turn1 = 0

for i in times1:
    interval += times1[i]
    if start != 0:
        if interval == 0:
            if0 = i
        elif interval == 1 and lastInterval == 0:
            turn1 = i
            if maxInterval < turn1 - if0:
                maxInterval = turn1 - if0
    if times1[i] == 1:
        if interval == 1:
            start = i
    elif times1[i] == -1:
        if interval == 0:
            end = i
            if maxMilking < end - start:
                maxMilking = end - start
    lastInterval = interval



f = open("milk2.out", "w")

f.write(str(maxMilking)+" "+str(maxInterval)+"\n")

# lineNumber = 1
#
# while lineNumber < len(values):
#     start, end = values[lineNumber].split()
#     start = int(start)
#     end = int(end)
#     if lineNumber == 1:
#         maxMilking = end - start
#     else:
#         if lastEnd > start:
#             maxMilking += (end - start) - (lastEnd - start)
#         else:
#             if maxMilking < end - start:
#                 maxMilking = end - start
#         if maxInterval < start-lastEnd:
#             maxInterval = start-lastEnd
#     lastEnd = end
#     lineNumber += 1
