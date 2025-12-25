import random
ComputerNumber=random.randrange(1,101)
guessInput = int(input("Enter the number"))
if ComputerNumber > guessInput:
    print(ComputerNumber)
    print("ComputerNumber is greater than guessInout")
elif ComputerNumber < guessInput:
    print(ComputerNumber)
    print("ComputerNumber is less than guessInout")
else:
    print(ComputerNumber)
    print("ComputerNumber is equal to guessInout")