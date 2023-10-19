"""
You're given an encrypted string for a secret password: tavaenryvahwribyv. You know that in order to get to this encrypted version of the password, the original password was run through a Caesar cipher and then reversed. Without knowing the key for the Caesar cipher, write a program to undo this encryption by printing out all 26 possibilities of the original password, and then take a guess at which of the possibilities is most likely to have been somebody's password.

"""

backpas = "tavaenryvahwribyv"
pas=[]
index = len(backpas)
while index > 0:
  pas += backpas[ index - 1 ]
  index = index - 1
print(pas)

dec_msg = ""
for i in range(26):
  for letter in pas:
    num = ord(letter)- i
    while num < 97:
      num += 26
    cha = chr(num)
    dec_msg += cha
  dec_msg += "      "

print (dec_msg)


# key to cipher = 15 and passcode is ilovejunilearning