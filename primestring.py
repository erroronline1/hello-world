"""check if string is prime as in
aaaa !prime
abab !prime
abcd prime"""

i=input('type in string to check if prime: ')
data={}
for chunk in range(2,len(i)+1):
	if not len(i)%chunk:
		pos=0
		data[chunk]=[]
		for step in range(1,chunk+1):
			rchunk=i[pos:pos+len(i)//chunk]
			if rchunk not in data[chunk]:
				data[chunk].append(rchunk)
			pos+=len(i)//chunk
			
print(data)
prime='input is prime'
for check in data:
	if len(data[check])<2:
		prime='input is not prime and consists of %d chunks of %s'%(check,data[check])

print(prime)
	