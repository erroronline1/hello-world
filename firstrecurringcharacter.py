"""
first recurring char in given input
i do not understand why i has to be
extended but it works: DON'T TOUCH IT
should perform well without nested loops
suggestions welcome!
"""
i=input('type something: ')
j={}
output=''
for c in '.'+i+'.':
	try:
		e=list(j.keys()).index(c)
		if e:
			output='character '+c+' was the first recurring'
			break
	except ValueError:
		j[c]=1
if output != '':
	print(output)
else:
	print('no recurring character found')
		