Problem 1: Name Organizer

Problem Statement:
    Write a Python program that asks the user to enter 5 names one by one and stores them in a list. Then:
    Sort the names alphabetically.
    Print the list of names.
    Ask the user to enter a name to search.
    Tell the user whether the name is in the list or not.

Example:

    Enter name 1: Riya
    Enter name 2: Aryan
    Enter name 3: Neha
    Enter name 4: Kabir
    Enter name 5: Zara

    Sorted names: ['Aryan', 'Kabir', 'Neha', 'Riya', 'Zara']

    Enter a name to search: Neha
    Neha is in the list!

Problem 2: Word Scrambler Game

Problem Statement:
    Write a Python program that scrambles a word and asks the user to guess the original word.
    Store any 3 words in a list (e.g. "apple", "banana", "grape").
    Pick one at random.
    Scramble its letters (e.g. "grape" → "argpe").
    Show the scrambled word to the user and let them guess.
    Tell them if they guessed it right or not.

Example:

    Guess the word: nagaba
    Your guess: banana
    Correct!

    Guess the word: pplea
    Your guess: apple
    Correct!

Hints:

    Use random.choice() to pick a word.
    Use random.shuffle() on a list of letters.
    Use ''.join() to convert list back to a word.