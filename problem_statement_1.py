# Number of items to buy

number_of_items = int(input("Please enter how many things you have to buy = "))
grocery_list = []
for i in range(number_of_items):
	grocery_list.append(input("Enter name of the item = "))

print("This is your grocery list = ",grocery_list)