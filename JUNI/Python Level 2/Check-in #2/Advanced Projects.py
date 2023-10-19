'''

Let’s see how big of a vocabulary our favorite authors (or lyricists) have! Ask the user to copy in a paragraph from their favorite book (or other piece of writing). Create a set of all the unique words, and print a message telling the user the number of different words contained in the paragraph out of the total number of words.

'''

x = "I like pie."
print(x.split("i"))

paragraph = set()


x = input("Copy and paste a paragraph from a book or song and see how many unique words are in it.")

x = x.replace(".", "")

for i in x.split():
  paragraph.add(i)

print("There are " + str(len(paragraph)) + " unique words in this paragraph.")
