#Immutable Objects : Tuples
# Tuples are immutable sequences, typically used to store collections of heterogeneous data. They are defined by enclosing the elements in parentheses `()` and separating them with commas.
# Once created, the elements of a tuple cannot be changed, making them suitable for use as dictionary keys or for storing fixed collections of items.
# Tuples can also be nested, meaning a tuple can contain other tuples as elements. This allows for the creation of complex data structures.
# Tuples are often used in Python for returning multiple values from a function, as they can hold a fixed number of items and maintain their order.


my_tuple = (1, 2, 3, 4, 5) # A tuple with five elements

print("Original Tuple:", my_tuple) # Output: Original Tuple: (1, 2, 3, 4, 5)
print("Type of my_tuple:", type(my_tuple)) # Output: Type of my_tuple: <class 'tuple'>
print("Length of my_tuple:", len(my_tuple)) # Output: Length of my_tuple: 5

print("First element of my_tuple:", my_tuple[0]) # Output: First element of my_tuple: 1
print("Last element of my_tuple:", my_tuple[-1]) # Output: Last element of my_tuple: 5

print("Slice of my_tuple (2nd to 4th element):", my_tuple[1:4]) # Output: Slice of my_tuple (2nd to 4th element): (2, 3, 4)

# Changing the value of an immutable object
#my_tuple[0] = 10 # This will raise a TypeError: 'tuple' object does not support item assignment

# Different ways to create a tuple
tuple1 = (1, 2, 3) # Using parentheses
tuple2 = 1, 2, 3 # Without parentheses (tuple packing)
tuple3 = tuple([1, 2, 3]) # Using the tuple() constructor
tuple4 = tuple(range(5)) # Creating a tuple from a range object
tuple5 = tuple("Hello") # Creating a tuple from a string (each character becomes an element)
tuple6 = (1,) # A single-element tuple (note the comma)
tuple7 = tuple() # An empty tuple
tuple8 = (1, 2, 3, (4, 5)) # Nested tuple
tuple9 = (1, 2, 3, [4, 5]) # Tuple with a list as an element
tuple10 = (1, 2, 3, {4: 'four', 5: 'five'}) # Tuple with a dictionary as an element

# Index function
print("Index of 2 in tuple1:", tuple1.index(2)) # Output: Index of 2 in tuple1: 1

# Count function
print("Count of 2 in tuple1:", tuple1.count(2)) # Output: Count of 2 in tuple1: 1

# Concatenation of tuples
tuple11 = tuple1 + tuple2 # Concatenating two tuples
print("Concatenated tuple:", tuple11) # Output: Concatenated tuple: (1, 2, 3, 1, 2, 3)

# Enumerate function
for index, value in enumerate(tuple1):
    print("Index: ",index, "Value: ",value) # Output: Index: 0, Value: 1 ... Index: 2, Value: 3

