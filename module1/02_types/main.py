"""
A type is how Python represents different types of data.
Integers -> 11 | int
Real Numbers -> 21.213 | float
Words -> "Hello Python 101" | str

We can see the actual data type in Python by using the type command.
type(11)
type(21.213)
type("Hello Python 101")

Integers can be negative or positive, it should be noted that there is a finite range of integers, but it is quite large.
Floats are real numbers; they include the integers but also numbers in between the integers.

You can change the type of the expression in Python, this is called type casting. You can convert an int to a float.

float(2) -> 2.0
int(1.1) -> 1
int('1') -> 1
int('A') -> error
str(1) -> "1"
str(4.5) -> "4.5"

Boolean is another important type in Python. A boolean can take on two values. The first value is true, just remember we use an uppercase T.
Boolean valus can also be false, with an uppercase F.

Using the type command on a Boolean value, we obtain theterm bool, this is short for boolean.
type(True) -> bool

You can convert a bool into a int too.
int(True) -> 1
And convert a int into a bool
bool(1) -> True
"""