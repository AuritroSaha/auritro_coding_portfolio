guests = []

guests.append("Tom")
guests.append("Joe")
guests.append("Bob")

guests.remove("Tom")

print(guests)

print(guests[0])

print("My guest list:")
print(guests[0])
print(guests[1])

print("My guest list:")
for i in guests:
  print(i)

num = []

for i in range(1,21):
  num.append(i)

print(num)

evens = []

for i in range(1,21):
  if i%2==0:
    evens.append(i)

print(evens)