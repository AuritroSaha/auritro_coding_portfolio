# Write function flipCoin() that returns either heads or tails randomly
import random

n = [1,2]

def flipCoin():
  x = random.choice(n)
  if x == 1:
    return 'Heads'
  if x == 2:
    return 'Tails'

flipCoin()

headcount = 0
tailcount = 0
numFlips = int(input("How many times do you want to flip a coin?: "))

for i in range(numFlips):
  m = flipCoin()
  if m == 'Heads':
    headcount += 1
  if m == 'Tails':
    tailcount += 1

print ("Number of times Heads was chosen: " + str(headcount))
print ("Number of times Tails was chosen: " + str(tailcount))

print('Percentage of times Heads was chosen: ' + str(headcount/numFlips*100) + '%')
print('Percentage of times Tails was chosen: ' + str(tailcount/numFlips*100) + '%')
