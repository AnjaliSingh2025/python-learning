# A class is a blueprint/template used to create objects.
# An object is a real instance of a class.
# self allows an object to access its own data and methods.
class DemoClass:
    a=10
    def sumValue(self):
        print(10+20)
demoobject=DemoClass()
objectcalling1=DemoClass()
objectcalling=demoobject.a
objectcallingpart2=objectcalling1.sumValue()
print(objectcallingpart2)
#A constructor is a special method that runs automatically when an object is created.
# In Python, the constructor is __init__().
# self refers to the current object calling the method.
# Encapsulation means hiding internal data and allowing access through methods.
class Employee:
    def __init__(self, name):
        self.name = name

e1 = Employee("Anjali")
e2 = Employee("x")

print(e1.name)
print(e2.name)
# Inheritance allows a child class to use parent class properties & methods.
class Employeess:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def role(self):
        print(self.name, "works with", self.language)

d = Developer("Anjali", "Python")
d.show()
d.role()
