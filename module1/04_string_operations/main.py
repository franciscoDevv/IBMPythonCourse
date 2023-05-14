# Strings
# In python a string is a sequence of charactrers

print("Hello")
print('Hello')
print("1 2 3 4 5 6")
print(")(#$/%)(#/)")
name = "Greedyboy"
print(name[0]) # Prints the first position on the variable name
name2 = name[0:2]
name3 = name[2:5]
print(f"Name1 -> {name}")
print(f"Name2 -> {name2}")
print(f"Name3 -> {name3}")
name4 = name2+name3
print(f"Name4 -> {name4}")
name5 = name[::2]
print(f"Name5 -> {name5}")

# Get the string size
print(len(name))
# Add strings to variables
print("Hello i am " + name)
# Multiply
print(3 * (name + " "))

#Print with new line
print("Hello\nhow are u?")
#Print with a tab
print("Hello\t how are u?")

# if we want to put a backslash on our print
print("Greedyboy \\ likes programming")

# STRING METHOS
text = "DummyAI is an AI that can help you on what you need"
text2 = text.upper()
print(f"Text before -> {text}")
print(f"Text after -> {text2}")

print("")
# We can replace with replace() too, it needs too arguments
text3 = text.replace("DummyAI", "usingReplaceMethod")
print(f"Text before -> {text}")
print(f"Text after -> {text3}")

#Using .find() method
print(text.find("AI"))