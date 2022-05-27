# WORDYL
# Guess a five letter word
# Iterate through letters in guess
# For each letter in guess, is it in secret?
# If it is, what position in secret is the letter?

import string
import random
import wordlist

secret = random.choice(wordlist.words)
guesses_remaining = 6
letters_remaining = string.ascii_lowercase


def guess_word():

  global guesses_remaining
  while guesses_remaining > 0:
  
    guess = input('Guess a 5-letter word:')
    print('\nGuesses remaining: {}'{guesses_remaining})
  
    if len(guess) == 5:
    
      if guess == secret:
        print('You win! The secret word is:\n\n>> {} <<'.format(secret))
        print('-' * 30)
        break
    
      for i in range(0, len(secret)):
    
        if secret[i] == guess[i]:
          print('[Correct pos]', guess[i]) # i+1 to show index
          # should actually hide index position, but indicate if it is right or wrong
  
        if guess[i] in secret and secret[i] != guess[i]:
          print('[Wrong pos]', guess[i])
  
        if guess[i] not in secret:
          print('[Not in word' , guess[i])
          #letters_remaining.replace(secret[i])
        
      print('-' * 30)
  
    
      guesses_remaining -= 1
  
    elif len(guess) != 5:
      print('You done messed up')
  
  if guesses_remaining == 0:
    print('Aw man, you lost!\nThe secret word is:\n\n>>{}<<'.format(secret))

guess_word()
