import time, random

'''
print("Starting a timer.")
start = time.time()
time.sleep(3)
end = time.time()
print(end-start)
'''

sentences = ["I saw Susie sitting in a shoe shine shop.", "I like to watch Marvel movies.", "Type faster you're so slow!"]

sentence = random.choice(sentences)

input("Welcome to Type Racer. Press Enter to play.")
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Type!")
print(sentence)
start = time.time()
x = input("Type: ")
end = time.time()



if len(sentence) != len(x):
  if len(sentence) >= len(x):
    print("You typed the sentence "+ str(len(x)/len(sentence)*100)+ "% correct.")
  elif len(x) > len(sentence):
    print("You typed the sentence "+ str(len(sentence)/len(x)*100)+ "% correct.")
else:
  print("You typed the sentence 100% correct.")

if x == sentence:
  print("You finished typing in " + str(end-start) + " seconds.")
else:
  l = sentence.split
  k = x.split
