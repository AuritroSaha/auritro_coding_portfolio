class BankAccount:
    def __init__(self, name, interest):
        self.owner = name
        self.interest = interest
        self.balance = 0

    def __str__(self):
        return "Name: " + self.owner + ", Interest Rate: " + str(self.interest) + "%" + ", Balance: $" + str(
            self.balance)

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, withdrawal):
        if withdrawal <= self.balance:
            self.balance -= withdrawal
        else:
            print("Transaction Rejected: balance overdrawn")

    def add_interest(self):
        self.balance = (self.interest / 100 + 1) * self.balance


x = BankAccount("Auritro", 2)
print(x)
x.deposit(50)
print(x)
x.withdraw(30)
x.add_interest()
print(x)
