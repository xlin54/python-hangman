from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words) # "TOUR"
    word_letters = set(word)    #{R, U, T, O}
    alphabet = set(string.ascii_letters)  #{N, E, A, ...}
    used_letters = set()  # what the user has guessed

    while len(word_letters) > 0:
        print('you have used these letters : ', ''.join(used_letters))
        # the current word, part u guess correctly show
        # part you did not guess yet, denote by -

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter : ').upper() # e , U
        if user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print(" you already used this character, try again : ")
        else:
            print(" invalid character, try again")
    print(" yay you guessed the word ",  user_letter ,' '.join(word_list))
    print(" yay you guessed the word ",  user_letter, word_list)
hangman()
