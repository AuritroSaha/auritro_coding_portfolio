'''
prices = {"soap": 2, "apple": 1, "frozen_pizza": 1}

print(prices["soap"])

print("apple" in prices)
print(2 in prices)

for item in prices.items():
  print(item)

prices["bread"] = 3
'''

'''
Create a dictionary where there are five key-value pairs. Each key should be a word in English language and each value should the word's definition. Then, print out the dictionary. 
'''

dictionary = {"banana": "yellow fruit", "shorts": "short pants", "games": "activities you do for fun; for entertainment", "dog": "furry animal that is usually a pet", "fingers": "the five wigglly things on each of your hands"}

for i in dictionary:
  print(i+": "+dictionary[i])


'''
Create a dictionary where the keys are the numbers 1 to 25 and the values are their squares. Then, print out the dictionary. 
'''

num_sqrs = {}

for i in range(1,26):
  num_sqrs[i] = i*i

for i in num_sqrs:
  print(str(i)+"'s square is "+str(num_sqrs[i]))
