# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound")


# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


# Another child class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


# Using the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()
