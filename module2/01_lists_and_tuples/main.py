"""
List and tuples are called compuond data types and are one of the keys types of data structures in Python.
"""

# T U P L E S
"""
- Tuples are an ordered sequence
- Tuples are written as comma-separated elements within parantheses
Ex:
Ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
"""

"""
All data types can be contained in a tuple, but the type of the variable is tuple.
Each element of a tuple can be accessed via an index.
"""

Tuple1 = ("disco", 10, 1.2)
print(Tuple1[0])
print(Tuple1[1])
print(Tuple1[2])

# In python we can use negative index.
print(Tuple1[-3])
print(Tuple1[-2])
print(Tuple1[-1])

# We can concatenate or combine tuples by adding them.

tuple2 = Tuple1 + ("hard rock", 10)

print("Slice a tuple:")
print(tuple2[0:3])
print("Slice the two last elements")
print(tuple2[3:5])

#Get the length of a Tuple
print(len(tuple2))

# Tuples are inmutable which means we can't change them
"""
As a consequence of inmutabulity. If we would like to manipulate a tuple, we must create a new tuple instead.
"""
numbers = (2, 5, 1, 512, 45)
SortedTuple = sorted(numbers)
print(SortedTuple)

# Nesting
"""
A tuple can contain other tuples a well as other complex data types; this is called nesting.
We can access these elemtns using the standart inedxing methods.
"""

nt = (1, 2, ("pop", "rock"), (3, 4), ("disco",(1,2)))
print(nt[2])
print(nt[2][1])
print(nt[2][1][0])


# L I S T S
"""
List are also a popular data structure in Python
List are also an ordered sequence.
Here is a list L. A list is represented with square brackets.
"""

l = ["Michael Jackson", 10.1, 1982]
print(l)
#Another example:
l2 = ["Michael Jackson", 10.1, 1982, [1,2], ('A', 1)]
print(l2)
l3 = ["Michael Jackson", 10.1, 1982, "MJ", 1]
print(l3[3:5])

# The index conventions for list and tuples are identical

l4 = l3 + [2, 3]
print(l4)

"""
Lists are mutablke, therefore, we can change them.
For example, we apply the method extens by adding a "dot" followed by the name of the method, then parenthesis.
The argument inside the parenthesis is a new list that we are goint to concatenate to the original list.
"""

l.extend(["new value", 7])
print(l)

# We can apply the append method to a list, if we apply append instead of extend, we add one element to the list
l.append(5)
print(l)

# As lists are mutable, we can change them
l[0] = "new text"
print(l)

"""
We can delete an element of a list using the 'del' command;
"""

del(l[0])
print(l)
del(l[1])
print(l)

# We can convert a string to a list using the method split
s = "I hope you are having a great day!"
newList = s.split()
print(newList)

"""
We can use the split function to separate strings on a specific character, known as a delimiter
"""

s2 = "A,B,C,D"
newList2 = s2.split(",")
print(newList2)

# Multiple names referring to the same object is known as aliasing
# If we have two list refering the same list, and we change one of them, the other one also changes

# You can clone a list using the next
b = newList[:]
# If you change NewList, b will not change