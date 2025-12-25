print(len("Python"))
print(len([10, 20, 30]))
print(len((1, 2)))
# Method Overriding (MOST IMPORTANT 🔥)
# Child class provides its own implementation of parent method.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

# Method overriding occurs when child class redefines parent method.
