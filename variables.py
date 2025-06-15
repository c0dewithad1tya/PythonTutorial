#Variables

#Global Variables
a = 5
b = 6

def addNumbers():
    # c here is a local variable to this function
    c = a + b
    print(c)

addNumbers()
#Fails
print(c)
