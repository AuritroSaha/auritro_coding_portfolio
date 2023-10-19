'''
message   key   cipher
-----------------------
pizza     1     qjaab
pizza     2     rkbbc
'''

# Encryption
msg = input("Give your name: ")
key = int(input("Give a key in between 1 and 25: "))
encr_msg = ""

#for i in range(len(msg)):
  #print(msg[i])

for letter in msg:
  num = ord(letter)+ key
  while num > 122:
    num -= 26
  print (num)
  cha = chr(num)
  encr_msg += cha

print (encr_msg)



# Decryption
key2 = int(input("Give the key: "))
encr_msg2 = input("Give the encrypted message: ")
dec_msg = ""

for letter in encr_msg2:
  num = ord(letter)- key
  while num < 97:
    num += 26
  print (num)
  cha = chr(num)
  dec_msg += cha

print (dec_msg)