# Mutable Data Types: Sets
# Sets are unordered collections of unique elements. They are mutable, meaning you can add or remove elements after creation. Sets are defined using curly braces `{}` or the `set()` constructor.
# Sets are useful for membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, and difference.
# Sets do not support indexing or slicing, as they are unordered collections. However, you can convert a set to a list or tuple if you need to access elements by index.
# Sets can contain elements of different data types, including other sets, but they cannot contain mutable objects like lists or dictionaries.

set1 = {1, 2, 3, 4, 5} # A set with five elements
set2 = {3, 4, 5, 6, 7} # Another set with five elements
set3 = set([1, 2, 3, 4, 5]) # Creating a set from a list
set4 = set("Hello") # Creating a set from a string (each character becomes an element) 
set5 = set() # An empty set
set6 = {1, 2, 3, (4, 5)} # Set with a tuple as an element
set7 = {1, 2, 3, [4, 5]} # This will raise a TypeError: unhashable type: 'list'
set8 = {1, 2, 3, {4: 'four', 5: 'five'}} # This will raise a TypeError: unhashable type: 'dict'

# Index function
print("Index of 2 in set1:", set1.index(2)) # This will raise an AttributeError: 'set' object has no attribute 'index'

# Count function
print("Count of 2 in set1:", set1.count(2)) # This will raise an AttributeError: 'set' object has no attribute 'count'

# Concatenation of sets
set9 = set1.union(set2) # Union of two sets
print("Union of set1 and set2:", set9) # Output: Union of set1 and set2: {1, 2, 3, 4, 5, 6, 7}

# Intersection of sets
set10 = set1.intersection(set2) # Intersection of two sets
print("Intersection of set1 and set2:", set10) # Output: Intersection of set1 and set2: {3, 4, 5}

# Difference of sets
set11 = set1.difference(set2) # Difference of two sets 
print("Difference of set1 and set2:", set11) # Output: Difference of set1 and set2: {1, 2}

set12 = set2.difference(set1) # Difference of two sets
print("Difference of set2 and set1:", set12) # Output: Difference of set2 and set1: {6, 7}