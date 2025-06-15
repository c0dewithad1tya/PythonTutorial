#Mutable Objects: These can be altered after creation, meaning their content can change without changing their identity.
#Mutable objects include: list, dict, set, bytearray, array.array

#Immutable Objects: Once created, these cannot be changed. Any modification results in the creation of a new object.
#Immutable objects include: int, float, bool, str, tuple, frozenset, bytes.

a = 10 #int
b = 10.5 #float
c = True #bool
d = "Hello" #str
e = (1, 2, 3) #tuple
f = frozenset([1, 2, 3]) #frozenset
g = bytes(5) #bytes
h = bytearray(5) #bytearray
j = [1, 2, 3] #list
k = {1, 2, 3} #set
l = {1: 'one', 2: 'two', 3: 'three'} #dict
m = None #NoneType
n = complex(1, 2) #complex 

#Changing the value of an immutable object

print(id(a)) # Memory address of the integer object
a = 20 # This creates a new integer object with value 20, rather than changing the original object.

print("Immutable Objects:")

print("a:", a) # 20
print(id(a)) # Memory address of the new integer object
