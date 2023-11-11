import random

def choose_word() :
    """
    Chooses a random word from a given list of words
    """
    words = ["programming", "function", "keyboard", "python", "hangman"]
    print(random.choice(words))
choose_word()