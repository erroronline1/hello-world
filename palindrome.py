"""
palindrome check
"""
s=''
while s!='x':
	s=input('palindrome? x to exit. ')
	print('it is' if s==''.join(list(reversed(s))) else 'it isn\'t')
else:
	print('have a nice day!')