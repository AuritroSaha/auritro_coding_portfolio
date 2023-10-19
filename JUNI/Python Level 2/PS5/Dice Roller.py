import random

n = [1,2,3,4,5,6]

def rollDice():
  g = random.choice(n)
  return g

numFlip = int(input("How many rolls do you want?: "))

p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
p10 = 0
p11 = 0
p12 = 0

for i in range(numFlip):
  r1 = rollDice()
  r2 = rollDice()
  if r1 + r2 == 2:
    p2 += 1
  if r1 + r2 == 3:
    p3 += 1
  if r1 + r2 == 4:
    p4 += 1
  if r1 + r2 == 5:
    p5 += 1
  if r1 + r2 == 6:
    p6 += 1
  if r1 + r2 == 7:
    p7 += 1
  if r1 + r2 == 8:
    p8 += 1
  if r1 + r2 == 9:
    p9 += 1
  if r1 + r2 == 10:
    p10 += 1
  if r1 + r2 == 11:
    p11 += 1
  if r1 + r2 == 12:
    p12 += 1

print ('The percentage that 2 was rolled is ' + str(p2/numFlip*100) + '%')
print ('The percentage that 3 was rolled is ' + str(p3/numFlip*100) + '%')
print ('The percentage that 4 was rolled is ' + str(p4/numFlip*100) + '%')
print ('The percentage that 5 was rolled is ' + str(p5/numFlip*100) + '%')
print ('The percentage that 6 was rolled is ' + str(p6/numFlip*100) + '%')
print ('The percentage that 7 was rolled is ' + str(p7/numFlip*100) + '%')
print ('The percentage that 8 was rolled is ' + str(p8/numFlip*100) + '%')
print ('The percentage that 9 was rolled is ' + str(p9/numFlip*100) + '%')
print ('The percentage that 10 was rolled is ' + str(p10/numFlip*100) + '%')
print ('The percentage that 11 was rolled is ' + str(p11/numFlip*100) + '%')
print ('The percentage that 12 was rolled is ' + str(p12/numFlip*100) + '%')
