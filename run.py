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

def display_word(word, guessed_letters):
    """
    Display the current state of the word, with underscores for unguessed letters
    and the guessed letters
    """
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def play_hangman():
    """
    Set up the game with allowed number of incorrect guesses.
    Check if the guess is right or wrong and let the user know.
    Check if the player has guessed all the letters or if the attempts have been reached.
    """
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print(display_word(word_to_guess, guessed_letters))
        guess = get_guess()

        if guess in word_to_guess:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess!")
            attempts -= 1
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    play_hangman()