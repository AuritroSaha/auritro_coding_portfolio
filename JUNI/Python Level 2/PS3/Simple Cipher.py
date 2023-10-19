'''
Functions:
  1. ord(): char -> ascii
  2. chr(): ascii -> char
'''

#print(ord('p'))
#print(chr(112))

'''
Hello -> 72 101 108 108 111
'''
msg = input("Give your name:" )
encr_msg = ""
key = 10

#for i in range(len(msg)):
  #print(msg[i])

for letter in msg:
  encr_msg += str(ord(letter)+ key) + " "
print (encr_msg)