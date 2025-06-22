print("Welcome to the Name Sorter!")
names = []

for i in range(5):
    name = input("Enter name - ")
    names.append(name)

names.sort()
print("Sorted names are: ", names)

search_name = input("Enter name to search: ")

if search_name in names:
    print(f"{search_name} is found in the list.")
else:
    print(f"{search_name} is not found in the list.")