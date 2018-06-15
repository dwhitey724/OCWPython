from ps3a import *
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    comp_words = []
    for i in range(0, len(hand)):
        comp_words.extend(get_perms(hand, i))

    comp_word_scores = [''] * len(comp_words)
    index = 0

    # Get scores for all word permutations. If real word, return word associated with max score. If not, return None
    for item in comp_words:
        if is_valid_word(item, hand, word_list):
            comp_word_scores[index] = get_word_score(item, HAND_SIZE)
            index += 1
        else:
            comp_word_scores[index] = 0
            index += 1
    if max(comp_word_scores) == 0:
        return None
    else:
        return comp_words[comp_word_scores.index(max(comp_word_scores))]


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    global score
    print('Current Hand: ' + display_hand(hand))
    print('')

    comp_word = comp_choose_word(hand, word_list)

    if comp_word is not None:
        comp_word_score = get_word_score(comp_word, HAND_SIZE)
        score += comp_word_score
        print("'{0}' earned {1} points. Total: {2} points".format(comp_word, comp_word_score, score))
        new_hand = update_hand(hand, comp_word)
        comp_play_hand(new_hand, word_list, score)

    else:
        print('Total Score: ' + str(score) + ' points')
        print('')


#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    score = 0
    count = 0

    new_hand = deal_hand(HAND_SIZE)
    last_hand = new_hand.copy()

    def first_choice():
        first_choice = input('Please input "n" to play new hand, "r" to replay last hand, or "e" to exit the game: ')
        return first_choice

    def second_choice():
        second_choice = input('Please input "u" for user to play the game and "c" for computer to play the game: ')
        return second_choice

    choice_one = first_choice()  # Initialize first question

    while choice_one != 'e':
        if choice_one == 'e':  # Breakout condition
            break

        elif choice_one == 'n':
            choice_two = second_choice()

            if choice_two == 'u':
                count += 1
                new_hand = deal_hand(HAND_SIZE)  # Deal new hand, use that
                last_hand = new_hand.copy()  # Store hand as last hand to replay
                play_hand(new_hand, word_list, score)
                choice_one = first_choice()

            elif choice_two == 'c':
                count += 1
                new_hand = deal_hand(HAND_SIZE)  # Deal new hand, use that
                last_hand = new_hand.copy()  # Store hand as last hand to replay
                comp_play_hand(new_hand, word_list, score)
                choice_one = first_choice()

            else:
                print('You have chosen an invalid option. Please try again.')
                choice_one = first_choice()

        elif choice_one == 'r' and count != 0:
            choice_two = second_choice()

            if choice_two == 'u':
                count += 1
                play_hand(last_hand, word_list, score)
                last_hand = new_hand.copy()
                choice_one = first_choice()

            elif choice_two == 'c':
                count += 1
                comp_play_hand(last_hand, word_list, score)
                last_hand = new_hand.copy()
                choice_one = first_choice()

            else:
                print('You have chosen an invalid option. Please try again.')
                choice_one = first_choice()

        elif choice_one == 'r' and count == 0:
            print('You have no hands to replay!')
            choice_one = first_choice()

        else:
            print('You have chosen an invalid option. Please try again.')
            choice_one = first_choice()

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

