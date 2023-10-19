def juni_latin(word):
    punc = ''
    if word[-1] in "?'.;,":
        punc = word[-1]
        word = word[:-1]
    first = word[0]
    word = word[1:]
    new = " "
    if punc == "." or punc == "?":
        new = "\n"
    word = word + first + "ay" + punc + new

    return word


f = open("input_punctuation.txt", "r")
a = open("juni_latin.txt", "w")

file_list = f.readlines()
input_list = []

for i in range(len(file_list)):
    for j in file_list[i].split():
        input_list.append(j)

for i in range(len(input_list)):
    a.write(juni_latin(input_list[i].strip()))