# 6.00 Problem Set 3
# 
# Hangman
#
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!


def hangman():

    word = choose_word(wordlist)
    print(word)
    letters = 'abcdefghijklmnopqrstuvwxyz'

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(word)) + " letters long.")

    def player_turn(word, turns, letters):
        """
        Represents a loop of play given a number of turns and the word to guess
        """
        guess_iterations = turns
        history = [None] * len(word)
        new_word = ['_'] * len(word)  # Empty list of previous correctly guessed letters

        for i in range(0, turns):
            print('-------------------------------------')
            print('You have ' + str(guess_iterations) + ' guesses left.')
            print('Available letters: ' + str(letters))
            guess = input('Please guess a letter: ').lower()

            u_word = underscore(word, guess, history, new_word)
            letters_left = unused_letters(letters, guess)
            letters = letters_left

            result = word.find(guess)

            if result == -1:
                print('Oops! That letter is not in my word: ' + u_word)
                guess_iterations -= 1
            else:
                print('Good guess: ' + u_word)

            print('Available letters: ' + str(letters_left))

            if word == u_word:
                print('Congratulations! You Win!')
                break
            elif guess_iterations == 0:
                print('Sorry, you lose.')
                break

    def underscore(word, guess, guess_history, underscore_word):
        """
        Makes underscored version of word. If guess is in word, replaces underscore with guess
        """

        print(guess_history)

        for i in range(len(word)):

            if guess_history[i] is not None:  # If letter exists in history, set it before checking new letter
                    underscore_word[i] = guess_history[i]

            if guess == word[i]:  # If letter guessed matches a letter in the word, set it
                underscore_word[i] = guess
                guess_history[i] = guess

        return ''.join(underscore_word)

    def unused_letters(letters, guess):
        """
        Strips the guess from the available letters list and returns what is left
        """
        new_letters = letters.replace(guess, "")
        return new_letters

    player_turn(word, 8, letters)


hangman()
