balances = {"auritrosaha": 0, "janesmith": 0, "bobsmith": 0}

logininfo = {"auritrosaha": "open123", "janesmith": "secret123", "bobsmith": "programm3r"}

while True:
    while True:
        print("Welcome to the bank! Please put your login info below: ")
        global x
        x = input("Username: ")
        y = input("Password: ")

        if x in logininfo and y == logininfo[x]:
            break

    print()
    print("Welcome " + x + "!\n")

    while True:
        print("You currently have $" + str(balances[
                                               x]) + " in your account. What would you like to do?\n\n\t1. Make a deposit\n\t2. Make a withdrawal\n\t3. Change your password\n\t4. Log out")
        x1 = int(input())

        if x1 == 1:
            y = int(input("Enter how much do you want to deposit: "))
            balances[x] = balances[x] + y

        if x1 == 2:
            y = int(input("Enter how much do you want to withdraw: "))
            balances[x] = balances[x] - y

        if x1 == 3:
            while True:
                y = input("Enter your password: ")
                if y in logininfo.values():
                    n = input("Now enter your new password: ")
                    logininfo[x] = n
                    print("Your password has been succesfully changed.")
                    break

        if x1 == 4:
            print("You have logged out of your account.")
            break

