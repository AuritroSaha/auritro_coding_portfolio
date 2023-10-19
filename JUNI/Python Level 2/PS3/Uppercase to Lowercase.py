'''
Ask user for a word in all uppercase, and convert this to lowercase.
'''

x = input("Give me an uppercase word: ")
msg = ""
pas = 32

def uppercase(string):
  return string.upper()

x = uppercase(x)

for i in x:
  msg += chr(ord(i) + pas)

print (msg)