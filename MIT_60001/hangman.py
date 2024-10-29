# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str = ""
    for letter in secret_word:
        if letter not in letters_guessed:
            str += "_"
        else:
            str += letter
    return str



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    str = string.ascii_lowercase
    for letter in letters_guessed:
        str = str.replace(letter, '')
    return str
    
def is_in_word(secret_word, guess):
    '''
    secret_word: string, the word the user is guessing
    guess: the letter guessed
    returns: boolean, True if guess is inside secret_word;
      False otherwise    
    '''
    for letter in secret_word:
        if letter == guess:
            return True
    return False

def unique_letters(word):
    l_str = ""
    count = 0
    for letter in word:
        if letter not in l_str:
            count += 1
            l_str += letter
    return count

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    len_sw = len(secret_word)
    print(f"I am thinking of a word that is {len_sw} letters long.")
    life = 6
    warn = 3
    letters_guessed = ""
    av_l = get_available_letters(letters_guessed)
    
    while not is_word_guessed(secret_word, letters_guessed) and life and warn:
        print("------------------------------------")
        print(f"You have {life} guesses left.")
        print(f"Available letters: {av_l}")
        guess = input("Please guess a letter: ")
        if not guess.isalpha() or len(guess) != 1:
            print("Please provide one letter.")
            warn -= 1
            if warn == 0:
                print(f"Sorry, you lose 1 guess.")
                life -= 1
                print(f"You have {life} guesses left.")
                warn = 3
            print(f"You have {warn} warnings left.")
        elif guess in letters_guessed:
            print("You guessed a letter that was guessed before.")
            warn -= 1
            if warn == 0:
                print(f"Sorry, you lose 1 guess.")
                life -= 1
                print(f"You have {life} guesses left.")
                warn = 3
            print(f"You have {warn} warnings left.")        
        else:
            letters_guessed += guess
            g_word = get_guessed_word(secret_word, letters_guessed)
            av_l = get_available_letters(letters_guessed)
            if is_in_word(secret_word, guess):
                print(f"Good guess: {g_word}")
            else:
                print(f"Oops! That letter is not in my word: {g_word}")
                life -= 1
                if guess in "aeiou":
                    life -=1
    if is_word_guessed(secret_word, letters_guessed):
        score = life * unique_letters(secret_word)
        print("------------")
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was else.")
        print(f"It waaassssssss: {secret_word}")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    other_word = other_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for mw_char, ow_char in zip(my_word, other_word):
        if mw_char != '_' and mw_char != ow_char:
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)
    if matches:
        print("Possible matches are:")
        #print(matches)
        print(" ".join(matches))
    else:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    len_sw = len(secret_word)
    print(f"I am thinking of a word that is {len_sw} letters long.")
    life = 6
    warn = 3
    letters_guessed = ""
    av_l = get_available_letters(letters_guessed)
    
    while not is_word_guessed(secret_word, letters_guessed) and life and warn:
        print("------------------------------------")
        print(f"You have {life} guesses left.")
        print(f"Available letters: {av_l}")
        guess = input("Please guess a letter: ")
        if guess == "*":
            show_possible_matches(g_word)
        elif not guess.isalpha() or len(guess) != 1:
            print("Please provide one letter.")
            warn -= 1
            if warn == 0:
                print(f"Sorry, you lose 1 guess.")
                life -= 1
                print(f"You have {life} guesses left.")
                warn = 3
            print(f"You have {warn} warnings left.")
        elif guess in letters_guessed:
            print("You guessed a letter that was guessed before.")
            warn -= 1
            if warn == 0:
                print(f"Sorry, you lose 1 guess.")
                life -= 1
                print(f"You have {life} guesses left.")
                warn = 3
            print(f"You have {warn} warnings left.")        
        else:
            letters_guessed += guess
            g_word = get_guessed_word(secret_word, letters_guessed)
            av_l = get_available_letters(letters_guessed)
            if is_in_word(secret_word, guess):
                print(f"Good guess: {g_word}")
            else:
                print(f"Oops! That letter is not in my word: {g_word}")
                life -= 1
                if guess in "aeiou":
                    life -=1
    if is_word_guessed(secret_word, letters_guessed):
        score = life * unique_letters(secret_word)
        print("------------")
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was else.")
        print(f"It waaassssssss: {secret_word}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

#    secret_word = 'apple'
#    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#    hangman(secret_word)
#    print(is_word_guessed(secret_word, letters_guessed))
#    print(get_guessed_word(secret_word, letters_guessed))
#    print(get_available_letters(letters_guessed))

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#   secret_word = choose_word(wordlist)
#   hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
