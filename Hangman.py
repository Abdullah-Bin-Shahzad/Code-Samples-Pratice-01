import random
import string
from words import words  # Assuming there is a file named 'words.py' with a list of words


def get_valid_word(words):
    '''Function to get a valid word for the game'''
    word = '-'
    # Loop until a word without '-' or ' ' is found
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

# Main hangman game function
def hangman():
    # Getting a valid word for the game
    word = get_valid_word(words)
    # Converting the word to a set of letters for easy tracking
    word_letters = set(word)
    # Generating a set of uppercase alphabets
    alphabets = set(string.ascii_uppercase)
    # Set to keep track of used letters
    used_letters = set()
    # Initial number of lives
    lives = 6
    # Printing the number of characters in the word
    print(f'This word is consist of {len(word)} characters')
    # Main game loop
    while len(word_letters)> 0 and lives != 0:
        
        print('You have', lives,'lives and you have used these letters',' '.join(used_letters))
        # Generating a list with letters if they are guessed, otherwise '-'
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current words',''.join(word_list))
        # Getting the user input for guessing a letter
        user_letter = input('Guess a letter: ').upper()
        # Checking if the input is a valid letter (in uppercase)
        if user_letter in alphabets-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print('Letter is not in word.')
        # If the letter is already used, informing the user to try again
        elif user_letter in user_letter:
            print('You have already used that charater. Please try again.')
        # If the input is not a valid letter, informing the user to try again
        else:
            print('Invalid character, Please try again.')

    # Game over, checking if the player won or lost
    if lives==0:
        print(f'You loss! The word is {word}')
    else: 
        print(f'You guessed it right {word}.')
# Starting the hangman game
hangman()