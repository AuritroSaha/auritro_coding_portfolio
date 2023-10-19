f = open("input.txt", "r")

input_dict = {}

input_list = f.readlines()

for i in range(len(input_list)):
  if i%2 == 0:
    input_dict[input_list[i].strip()] = input_list[i+1].strip()

print(input_dict)