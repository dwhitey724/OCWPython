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
        for i in range(0, turns):
            print('-------------------------------------')
            print('You have ' + str(guess_iterations) + ' guesses left.')
            print('Available letters: ' + str(letters))
            guess = input('Please guess a letter: ')

            u_word = underscore(word, guess)
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


    def underscore(word, guess):
        """
        word (str): the word chosen by the game
        guess (str): the letter guessed by the player
        returns a list representation of the unfilled and filled in letters
        """
        word_list = ['_' if guess not in word else guess]
        return str(word_list)

    def unused_letters(letters, guess):
        """
        Strips the guess from the available letters list and returns what is left
        """
        letters_list = list(letters)
        letters = letters_list.remove(guess)
        return str(letters_list)

    player_turn(word, 8, letters)


hangman()
