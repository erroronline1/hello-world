"""
guess the number. first but later improved python experiment
"""
from random import randint
min=0
max=9
print('guess my number between {0} and {1}. type x to exit.'.format(min,max))
guessno=1
guess=''
sol=randint(min,max)
while True:
	guess=input('your guess? ')
	try:
		guess=int(guess)
	except ValueError:
		if guess=='x':
			print('have a nice day!')
			break
		else:
			print('numbers only please...')
			continue
	if guess<sol:
		guessno+=1
		print('too small...')
	elif guess>sol:
		guessno+=1
		print('too big...')
	else:
		print('it took you {0} attempts to guess my number.'.format(guessno))
		if guessno==1:
			print('brilliant!')
		break
		