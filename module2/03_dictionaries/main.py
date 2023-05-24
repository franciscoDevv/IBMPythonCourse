# Dictionary

"""
A dictionary has keys and values.
The key is analougous to the index, they are like addresses but they don't have to be integers. THey are usually characters; the values are similar to the elements in a list and contain information.

"""

# Example of a dictionary
dic = {"Gabriel": 4, "Martin": 16, "Jose": 41}
print(dic)
print(dic["Gabriel"])
# Add new value
print("Adding new value...")
dic["Pepe"] = 23
print(dic)
# Delete a value
print("Deleting a value...")
del(dic["Gabriel"])
print(dic)
# Check if an element is in a dictionary
print("Pepe" in dic)
# Print the dictionary keys
print(dic.keys())
# Print the dictionary values
print(dic.values())