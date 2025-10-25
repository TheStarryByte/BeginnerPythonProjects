import random
from words import words
import string

def valid_word(words): # first we need to choose a world without - or space
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_word(words).upper()
    word_letters = set(word) # all the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # all the alphabet that has been guessed

    lives = 7 # how many guesses the user have in total

    # now we should get user input
    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, 'lives left and you have used these letters:', ''.join(used_letters))

        # the current word for example S--F--A
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letters = input('Please enter a letter: ').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
                print('')

            else:
                lives = lives - 1
                print('Sorry, Your letter was not in the word')

        elif user_letters in used_letters:
            print('You have already used that letter')

        else:
            print('That is not a valid letter')

    #last part when lives ==0
    if lives == 0:
        print('YOU DIED , THE WORD WAS', word)
    else:
        print('YOU WON THE WORD WAS', word)

if __name__ == '__main__':
     hangman()

