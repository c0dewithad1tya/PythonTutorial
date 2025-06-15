'''
Problem Statement: Check if a string is a palindrome.
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward
(ignoring spaces, punctuation, and capitalization).
Example: madam, racecar, 12321, A, "Able was I ere I saw Elba"
'''

user_string = input("Enter a string: ")

user_string = user_string.lower()  # Convert to lowercase to ignore case
user_string = ''.join(user_string.split())  # Remove spaces
user_string = ''.join(char for char in user_string if char.isalnum())  # Remove punctuation

print("Original String (ignoring spaces, punctuation, and capitalization) - ",user_string)
reversed_string = user_string[::-1]

print("Reveresed String - ",reversed_string)
if user_string == reversed_string:
    print("String is a palindrome")
else:
    print("String is not a palindrome")