import random

def choose_word() :
    """
    Chooses a random word from a given list of words
    """
    words = ["programming", "function", "keyboard", "python", "hangman"]
    return random.choice(words)

def get_guess(guessed_letters):
    """
    Ask for a letter input from the user and make it lower case.
    Check that the letter has not been introduced yet.
    Check that is a letter.
    """
    while True:

        guess = input("Enter a letter: \n").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You have already tried that letter. Try again.")
            else:
                return guess
        else:
            print("invalid input. Please enter a single letter.")       

def display_word(word, guessed_letters):
    """
    Display the current state of the word, with underscores for unguessed letters
    and the guessed letters
    """
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def display_tried_letters(guessed_letters):
    """
    Display the letters that have been tried
    """
    if guessed_letters:
        print("Tried letters:", ','.join(guessed_letters))
    else:
        print("No letters tried yet.")

def display_attempts(attempts):
    """
    Display the number of attempts left"
    """
    print(f"Attempts left: {attempts}")

def play_again():
    """
    Ask the user if he wants to play again
    """
    return input("Do you want to play again? (yes/no): ").lower == "yes"

def play_hangman():
    """
    Set up the game with allowed number of incorrect guesses.
    Ask the player for name input.
    Check if the guess is right or wrong and let the user know.
    Check if the player has guessed all the letters or if the attempts have been reached.
    Ask the player if he wants to play again.
    """
    while True:
        player_name = input("Enter your name: \n")
        print(f"Welcome to Hangman, {player_name}!")

        word_to_guess = choose_word()
        guessed_letters = []
        attempts = 6


        while attempts > 0:
            print(display_word(word_to_guess, guessed_letters))
            display_tried_letters(guessed_letters)
            display_attempts(attempts)
            guess = get_guess(guessed_letters)

            guessed_letters.append(guess)

            if guess in word_to_guess:
                print("Good guess!")
            else:
                print("Incorrect guess!")
                attempts -= 1
            
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations, {player_name}! You guessed the word:", word_to_guess)
                break

        if attempts == 0:
            print(f"Sorry,{player_name}, you ran out of attempts. The word was:", word_to_guess)

        if not play_again():
            print("Thank you for playing Hangman! Goodbye.")
            break

if __name__ == "__main__":
    play_hangman()