import random


# Define a class
class Dog:

    # Initialization Method/Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
        self.tricks = ["play"]
        self.issitting = False

    def __str__(self):
        return "Name: " + self.name + " | Age: " + str(self.age) + " | Tricks: " + str(self.tricks)

    # Instance Method
    def learn_trick(self, trick):
        self.tricks.append(trick)

    def do_trick(self):
        x = "Your dog doesn't know any tricks."
        if len(self.tricks) != 0:
            x = random.choice(self.tricks)
        return x

    def sit_down(self):
        self.issitting = True

    def stand_up(self):
        self.issitting = False

    def get_state(self):
        if self.issitting == True:
            print("Sitting")
        else:
            print("Standing")


# Initialize an instance of Dog class

x = Dog("Marty", 4)  # Dog object

print(x.tricks)
x.learn_trick("fetch")
print(x.tricks)

print(x.do_trick())
print(x)

x.sit_down()
x.get_state()
