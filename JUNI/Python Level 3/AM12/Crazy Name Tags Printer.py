name = input("What's your name?: ")

f = open("Crazy Name", "w+")
for i in name:
  f.write(str(i)+"\n")
f.write("\n")
for i in range(len(name)):
  if i%2 == 0:
    f.write(str(name[i])+"\n")
f.write("\n")
for i in range(len(name)):
  i=i+1
  f.write(str(name[-i])+"\n")
f.close()