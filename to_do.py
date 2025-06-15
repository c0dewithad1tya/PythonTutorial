'''
    Write code for implementing a TO-DO List
    1. User can add an item/task
    2. User can delete the task/item
    3. User can also update the name of the item
    4. User can see all the items/task in their to-do list
'''
to_do = []
print("Welcome to Arnav's world. What do I need to do for today!?")

flag = True
while flag:
    print("You get four operations - Add Item, Delete Item, Update Item, Display List, End")

    life = input("Enter an operation = ")

    match life:
        case 'Add Item':
            task = input("Enter new task - ")
            to_do.append(task)
            print("Task added to the list.")
        case 'Delete Item':
            delete_task = input("Enter the task name to delete = ")
            to_do.remove(delete_task)
        case 'Update Item':
            update_task = input("Enter the task name which needs to be updated = ")
            new_task = input("Enter the new task name = ")
            for i,item in enumerate(to_do):
                 if item==update_task:
                    to_do[i]=new_task
                    print("Item Updated to ",new_task)
        case 'Display List':
            print("Here's your to-do list = ",to_do)
        case 'End':
            flag = False
        case _:
            print("Select correct operation!")
