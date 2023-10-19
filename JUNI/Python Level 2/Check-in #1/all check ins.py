word = "animal"

num = 42

print(word)

print(num)

num = str(num)

a = input("Guess an animal: ")

c = input("Now guess the color of the animal: ")

length = len(a)

print (length)

print(c[2])

# This line prints what the user chose as an animal and its color
print ("You guessed " + a + " and the color " + c)

for i in range(11):
  print(i)

clen = len(c)

for i in range(clen):
  print(c[i])

for i in range(6,16,3):
  print(i)

p = 0

while p<16:
  print(p)
  p = p + 1

q = 1

while q<length:
  if q%2 == 1:
    print(a[q])
  q = q + 1

k = 1

while True:
  print(k)
  k += 1
  if k == 11:
    break

if a == "cat":
  print("We love cats!")

if a == "dog" and c == "black":
  print("correct answer")

elif a == "dog" or c == "black":
  print("almost there")

else:
  print("wrong answer")
