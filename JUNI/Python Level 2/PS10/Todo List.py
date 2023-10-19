print("Welcome to your todo list!")

todolist = []

while True:
    print()
    print("What would you like to do with your list?")
    print()
    print(" 1. Add a task")
    print(" 2. Remove a task")
    print(" 3. Exit")
    print()
    x = int(input("Type in the number here: "))

    if x == 1:
        y = input("Please type what you want to add to your todo list: ")
        todolist.append(y)

    elif x == 2:
        y = int(input("Please type the number of what you want to remove: "))
        todolist.remove(todolist[y - 1])

    elif x == 3:
        break

    n = 1

    print("Here's your updated list:")
    print()
    for i in todolist:
        print(str(n) + ". " + str(i))
        n = n + 1

