# Object-Oriented approach
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # The actual implementation will vary for each animal

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of classes
animals = [Dog("Buddy"), Dog("Max"), Dog("Charlie"), Cat("Whiskers"), Cat("Oliver"), Cat("Luna")]

print("Animal sounds:")
for animal in animals:
    print(animal.name, "says:", animal.speak())
