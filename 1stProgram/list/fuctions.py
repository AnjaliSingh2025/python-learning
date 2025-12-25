# Functions is resuable block of code that performs a task
# Function is independent, method is associated with an object.
# we can pass data known as parameters into a  function
# In python function is defined using a def keyword


from optparse import Values


def showdata():
    print("Welocome to wscubetech")
showdata()


# function with arguments

def sum(num1, num2):
    print(num1+num2)

sum(40,50)
sum(70,40)


# Default argument
def minus(num1, num2=30):
    print(num1-num2)
minus(100)

# Return Values
def square(x):
    return x*x,x*2
s=square(4)
print(s)