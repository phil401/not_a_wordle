# sort of a wordle situation
import string
import random
import secrets

# replace used letters with - 
letters_remaining = string.ascii_lowercase

secrets = secrets.secrets
secret = random.choice(secrets)
guesses = 6
attempt = []

def guess_word():

	global guesses

	while guesses > 0:

		print('Guesses remaining: {}'.format(guesses))
		guess = input('''
	*************************
	Guess a five-letter word:
	*************************
	''')
		if guess == secret:
			print('''
	************************
	You guessed it!
	The secret word is {}
	************************
			'''.format(secret))
			break

		if len(guess) == 5:

			for g in guess:
			
				if g in secret:
					s = secret.index(g) + 1
					print(s, g)
					attempt.append(g)
				
				elif g not in secret:
					print('-')
					#attempt.append('-')

		print(attempt[-6:-1])
		print('Letters remaining: {}'.format(letters_remaining))
		guesses -= 1

	print('''
	Game over!\n
	''')

guess_word()
