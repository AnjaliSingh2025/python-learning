# # Encapsulation means hiding internal data and allowing access through methods.
# When a child class provides its own implementation of a method that already exists in the parent class.
# Type	Syntax	Meaning
# Public	var	Accessible everywhere
# Protected	_var	Child classes allowed
# Private	__var	Class only

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

acc = BankAccount(5000)

print(acc.show_balance())  # ✅ allowed
acc.deposit(2000)
print(acc.show_balance())

