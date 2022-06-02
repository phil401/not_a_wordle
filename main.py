# WORDYL
# Guess a five letter word
# Iterate through letters in guess
# For each letter in guess, is it in secret?
# If it is, what position in secret is the letter?

import string
import random
import wordlist

secret = random.choice(wordlist.words)

line = '-'*20
sline = '*'*20

def guess_word():

    guesses_remaining = 6
    letters_remaining = string.ascii_lowercase

    while guesses_remaining != 0:
        print('\nGuesses remaining: {}'.format(guesses_remaining))
        print('\nLetters remaining:\n{}\n{}\n'.format(line, letters_remaining))
        guess = input('Guess a 5-letter word:')

        if len(guess) == 5:

            if guess == secret:
                print('You win! The secret word is:\n\n>> {} <<'.format(secret))
                print(line)
                break

            for i in range(0, len(secret)):

                if guess[i] == secret[i]:
                    print('+{}+'.format(guess[i])) # i+1 to show index
                    letters_remaining = letters_remaining.replace(guess[i], '[{}]'.format(guess[i].upper()))

                if guess[i] in secret and secret[i] != guess[i]:
                    print('({})'.format(guess[i]))
                    letters_remaining = letters_remaining.replace(guess[i], '({})'.format(guess[i].upper()))


                if guess[i] not in secret:
                    print('-{}-'.format(guess[i]))
                    #letters_remaining.replace(secret[i])
                    letters_remaining = letters_remaining.replace(guess[i], '-{}-'.format(guess[i]))



            print(line)


            guesses_remaining -= 1

        elif len(guess) != 5:
          print('{}\nYou done messed up, honky!\n{}'.format(line, line))

    if guesses_remaining == 0:
        print('{}\nAw man, you lost!\nThe secret word is:\n\n>>{}<<\n{}'.format(line, secret, line))

guess_word()
