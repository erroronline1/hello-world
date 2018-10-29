"""
find a pair of numbers in a list that add up to a number given by user
For example, for the numbers [1, 2, 4, 4]:
Input: 8 Output: True
Input: 7 Output: False
"""
from random import randint
import math
max=9
add=[randint(-max,max) for i in range(0,2*max)]
add.sort()
ui=int(input('please type a number between 2 and %d: '%(max*2)))
print('this is a later ordered generated list of random integers: ',add)
found=False
for i in add:
	add2=add
	add2.pop(add.index(i))
	if ui-i in add2:
		print('first pair found as %d and %d' %(i,ui-i))
		found=True
		break
if not found:
	print('sorry, no pair found.')