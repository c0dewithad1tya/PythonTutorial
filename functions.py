# This is tutorial for funcions in Python

# Write a function which prints your Name, age and city

def print_personal_info(name, age, city):
    print("Inside the function print_personal_info")
    """
    Prints the personal information of a person.
    
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    city (str): The city where the person lives.
    """
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Example usage
if __name__ == "__main__":
    print("Outside the function print_personal_info")
    print_personal_info("John Doe", 30, "New York")
    print_personal_info("Alice Smith", 25, "Los Angeles")
    print_personal_info("Bob Johnson", 40, "Chicago")
    print_personal_info("Arnav", 14, "Bergen")
    print_personal_info("Siddharth", 15)
