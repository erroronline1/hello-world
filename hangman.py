"""
hangman. second python experiment
"""
from random import randint
list=('bar','house','table','foo')
sol=list[randint(0,len(list)-1)]
length=len(sol)
print('guess a word with {0} letters.'.format(length))
wrong=[]
right=[]
while len(wrong)<len(sol):
	char=input('guess letter: ')
	if len(char) >1:
		print('only one letter per guess please...')
	elif char in wrong:
		guessno=wrong.index(char)+1
		language=('st','nd','rd','th')
		if guessno<4:
			guessno=str(guessno)+language[guessno-1]
		else:
			guessno=str(guessno)+language[3]
		print('this was already your {0} false guess.'.format(guessno))
	elif char in right:
		print('you had this one already.')
	elif char not in sol:
		wrong.append(char)
		print('sorry, not sorry, {0} faults left'.format(len(sol)-len(wrong)))
	else:
		print('educated guess!')
		right.append(char)
		hint=''
		for c in sol:
			if c in right:
				hint+=c
			else:
				hint+='_'
		if hint==sol:
			print('you won! the solution is',sol)
			break
		else:
			print('hint: ', hint)
else:
	print('you lost :(')