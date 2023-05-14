"""
Expressions are operations that Python permos. For example, basic arithmetic operations like
43 + 60 + 16 + 41
"""
print(43 + 60 + 16 + 41)

"""
We call the numbers operands an the maths symbols in this case addition, are calle operators.
"""

print(50-60)
print(5 * 5)
print(25 / 5)

# Now check this case
print(25/6)
"""
25 dividied by 6 is approximately 4.167
In Python 3, both will result in a float
"""

"""
We can use the oduble slash for integer division, where the result is rounded.
"""
print("")
# Python follows mathematical conventions when performing mathematical expressions.
print(2*60+30) # same result
print(30+2*60) # same result

# The expressions in the parentheses are performed first. We then multiply the result by 60
print((30+2)*60)

# V A R I A B L E S
"""
We can use variables to store values. In this case. We assign a value of 1 to the variable.
"""
myVariable = 1
print(f"Variable -> {myVariable}")
# We can reassign its value
myVariable = 3
print(f"Variable's new value -> {myVariable}")

# We can also assign a expression to a variable
x = 43 + 60 + 16 + 41
print(x)
y = 2.6666
x = x/60
print(type(x))

# Example:
totalMinutes = 43 + 42
totalHours = totalMinutes / 60
print(f"Total minutes -> {totalMinutes}")
print(f"Total hours -> {totalHours}")