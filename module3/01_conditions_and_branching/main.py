"""
Compmarison operations compare some value or operand, then, based on some condition they produce a Boolean.
"""
# Conditions

# Let's say we assign "a" value of "a" to 6
a = 6
# We can use the equality operator denoted with two equal signs to determine if two values are equal
print(a == 6) # Prints true
print(a == 7) # Prints false

print(a > 5)
print(a != 3)

# Branching
"""
Branching allows us to run different statements for a different input
"""

# If statement
age = int(input())
if age > 18:
    print("you can enter")
    
# Else state,emt
if age > 18:
    print("you can enter")
else:
    print("you can't, bye bye")
    
# Elif statement
if age > 18:
    print("you can enter")
elif age == 18:
    print("you are 18, almost")
else:
    print("cya!")

# Logic Operators

#Not
print(not(False))

# or
if age <18 or age == 18:
    print("you are not 19 or older")
# and
if 5 < 6 and 5 < 7:
    print("yea, it is!")