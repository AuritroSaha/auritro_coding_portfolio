riders = []

for i in range(10):
  x = input("Enter rider "+ str(i+1) + "'s weigth (or q to quit): ")
  if x == "q":
    break
  riders.append(x)

def ridersdata(x):
  print("The list of the riders weights is: ")
  print(x)
  ride = 0
  for i in x:
    ride += int(i)
  print("The total weight of the riders is: " + str(ride))
  ride2 = ride/len(x)
  print("The average weight of the riders is: " + str(ride2))

ridersdata(riders)
