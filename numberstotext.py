"""
exercise for writing out positive integers
in english. chunk_two can be extended.
"""
#language model
chunk_one=('','one',('two','twen'),('three','thir'),'four',('five','fif'),'six','seven',('eight','eigh'),'nine')
chunk_two=('teen','ty','hundred','thousand','million','billion')
exception={10:'ten', 11:'eleven',12:'twelve'}
num=None

"""
numbers up to 99 because of language
inconsistencies
"""
def to99(n):
	if n in exception:
		return exception[n]
	else:
		if n<10:
			if n in (2,3,5,8):
				return chunk_one[n][0]
			else:
				return chunk_one[n]
		elif n<20:
			if n-10 in (2,3,5,8):
				return chunk_one[n-10][1]+chunk_two[0]
			else:
				return chunk_one[n-10]+chunk_two[0]
		else:
			dec=int(n//10)
			uno=int(n%10)
			if dec in (2,3,5,8):
				temp= chunk_one[dec][1]+chunk_two[1]
			else:
				temp= chunk_one[dec]+chunk_two[1]
			if uno in (2,3,5,8):
				return temp+chunk_one[uno][0]
			else:
				return temp+chunk_one[uno]

def hundred(n):
	h=int(n//100)
	d=int(n%100)
	output=''
	if h>0:
		output+=' '+to99(h)+chunk_two[2]
	if d>0:
		output+=' '+to99(d)
	return output

while num!= 0:
	num=int(input('integer up to 10^{0}, 0 to exit:  '.format(len(chunk_two))))
	#blocks of 10^3^x
	blocks=len(str(num))//3
	#incomplete blocks
	icblocks=len(str(num))%3

	output=''
	t1=0
	if icblocks>0:
		t1=len(str(num))-blocks*3
		icblock=str(num)[0:t1]
		if blocks>0:
			output+=hundred(int(icblock))+' '+chunk_two[blocks+2]
		else:
			output+=hundred(int(icblock))
	if blocks>0:	
		loops=list(range(blocks))
		for i in loops:
			step=t1+i*3
			block=str(num)[step:step+3]
			if int(block)>0:
				if i==blocks-1:
					output+=hundred(int(block))	
				else:
						output+=hundred(int(block))+' '+chunk_two[len(chunk_two)-i-2]
	print(output)
else:
	print('goodbye')