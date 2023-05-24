# S E T S
""""
Sets are also a type of collection. This means that lke list and tuples, you can input different python types. Unlike list and tuples they are unordered.
This means sets do not record element position, Sets only have unique elements.

This means there is opnly one of a particular element in a set.
"""

# Define a set
set1 = {"mackana", "luna", "avion", "luz", "luna", "sol", "sol"}
print("Not repetead elements")
print(set1)

"""
You can convert a list to a set by using the function set; this is called type-casting
"""

l = [2, 4, 4, 4, 3]
setL = set(l)
print(setL)
# print(set(list))


# SET OPERATIONS

q = {"Luffy", "Zoro", "Nami"}
# We can add a element to a set using the .add() method
q.add("Usopp")
print(q)
# We can remove an element from a set using the .remove() method
q.remove("Nami")
print(q)

"""
We can verfy if an element is in the set using the 'in' command. THe command checks if the item is in the set, it returns true.
"""
print("Zoro" in q)
print("Whitebeard" in q)

q2 = {"Zoro", "Luffy", "Ace", "Sabo"}
q3 = q & q2
print(q3)