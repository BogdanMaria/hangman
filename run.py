import random

def choose_word() :
    """
    Chooses a random word from a given list of words
    """
    words = ["programming", "function", "keyboard", "python", "hangman"]
    return random.choice(words)

def get_guess():
    """
    Ask for a letter input from the user and make it lower case
    """
    return input("Enter a letter: ").lower()
get_guess()