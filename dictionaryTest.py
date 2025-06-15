to_do = {
    "Complete homework":'To Do',
    "Go to gym" :'To Do',
    "Read a book" :'To Do'
}

print("To-Do List:", to_do)

user_input = input("Enter a task to add to the list: ")
to_do[user_input] = 'To Do'

print("Updated To-Do List:", to_do)

user_input = input("Enter a task to delete from the list: ")
if user_input in to_do:
    del to_do[user_input]
else:
    print(f"Task '{user_input}' not found in the list.")

print("Updated To-Do List:", to_do)

#Update the status of a task
task_to_update = input("Enter a task to update its status: ")
if task_to_update in to_do:
    new_status = input("Enter the new status (To Do/In Progress/Done): ")
    to_do[task_to_update] = new_status
else:
    print(f"Task '{task_to_update}' not found in the list.")

print("Updated To-Do List:", to_do)
#Display all tasks in the list