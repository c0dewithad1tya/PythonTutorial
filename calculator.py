'''This is a Calculator
 We take 2 numbers as input from user
 Then we ask which Mathematical Operation they want to perform
 (Addition.Substraction, Division, Multiplication)
'''
answer = input("Want to Calculate something? (Y/N) ")

if answer == 'Y':
    num1 = int(input("Enter first number = "))
    num2 = int(input("Enter second number = "))
    operation = input("Addition/Substraction/Multiplication/Division? ")

    if operation == 'Addition':
        print("Calculated Value = ",num1+num2)
    elif operation == 'Substraction':
        print("Calculated Value = ",num1-num2)
    elif operation == 'Multiplication':
        print("Calculated Value = ",num1*num2)
    elif operation == 'Division':
        print("Calculated Value = ",num1/num2)
    else:
        print("You didnt pick the correct operation")
else:
    print("Bye! Maybe I can help next time!")