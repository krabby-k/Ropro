class Dog:

    # class attribute
    species = 'mammal'

    # initializer / instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# child class inherit attributes
# and behaviors from the parent class
jim = Bulldog('jim', 12)
print(jim.description())

# child class have specific attributes
# and behaviors as well
print(jim.run("slowly"))