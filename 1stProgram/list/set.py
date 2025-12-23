# Sets are unordered collections.
# Duplicate values are automatically removed
# You can add or remove elements
# But you cannot change individual elements
s={10,20,30,40}
# Adds one element.
s.add(50)
print(s)
# Update
# Adds multiple elements.
u = {1, 2}
u.update([3,4])
print(u)

S = {10,20,30,40}
for a in S:
    print(a)

# S = {10, 20, 30, 40}
# for a in S:
#     print(a)

# some imp set functions
# Set()
# Add()
# Pop()
# Remove()
# Clear()
# Discard()
# Update()
l=[10,20,30,40]
s = set(l)
print(s)

# update function use
K = { 10, 20, 30, 40}
p = s.pop()
print(K) 

# Remove function of set 
R = { 10, 20, 30, 40}
r = R.remove(30)
print(R) 
# discard function use
D = { 10, 20, 30, 40}
d = D.discard(30)
print(D) 

C={10, 20, 40, 60, 70, 80}
c=C.clear()
print(C)

U={50, 60, 70, 40, 60}
l=[100, 400]
an=U.update(l)
print(U)