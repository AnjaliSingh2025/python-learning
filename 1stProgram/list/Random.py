# The random module is a built‑in Python module used to generate random numbers or random selections.commonly used in Games 🎮

# Simulations

# Data sampling

# Password / OTP generation

import random 
# print(random.random())

# randint(a, b) 
# Returns a random integer between a and b (inclusive)
# print(random.randint(1, 10))
# # randrange(start, stop, step)
# random.randrange(1, 10, 2)

# choice(sequence) 
# Returns one random element from a list, tuple, or string

print(random.choice([10, 20, 30]))
print(random.choice("PYTHON"))
# Returns multiple random elements (with replacement)
random.choices([1, 2, 3], k=2)
print(random.choices([1, 2, 3], k=2))
print(random.randint(100000, 999999))
l=[10,20,30,40]
random.shuffle(l)
print(l)
u=random.uniform(3,9)
print(u)