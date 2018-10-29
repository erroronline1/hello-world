# practices according to practicepython.org
# 1. input name and age and calculate when user turns 100
def lesson_one(): 
    from datetime import datetime
    name=input('what is your name? ')
    age=int(input('what is your current age? '))
    year=str(datetime.now().year-age+100) 
    print('hello {0}, you would turn 100 in the year {1}.'.format(name,year))
#lesson_one() 

# 2. is input number odd or even?
def lesson_two(): 
    num=int(input('what number do you want to check? '))
    print('odd' if num%2 else 'even')
#lesson_two() 

# 3. take a list and output any number less than x (by input) / one line / multiline
def lesson_three(): 
    from random import randint
    max=29 
    l=[] 
    for i in range(10): 
        l.append(randint(0,max))
    limit=int(input('your limit between 0 and '+str(max)+': '))
    l.sort() 
    for i in l: 
        if i<limit: 
            print(i,' ',end='')
#lesson_three() 

# 4. calculate even divisors
def lesson_four(): 
    num=int(input('test for divisors: '))
    div=[] 
    for i in range(2,num): 
        if not num%i: 
            div.append(i) 
    if len(div): 
        print ('divisors are ',end='')
        print(div) 
    else: 
        print('you typed in a prime!')    
#lesson_four() 

# 5. compare two lists and return common elements without duplicates (random lists)
def lesson_five(): 
    from random import randint
    max=15 
    list1=[] 
    list2=[] 
    for i in range(0,randint(5,max)):
        list1.append(randint(0,max))
        list2.append(randint(0,max))
    print(set(list1) & set(list2))
#lesson_five() 

# 6. check input for being a palindrome or not
def lesson_six(): 
    s='' 
    while s!='x': 
        s=input('palindrome? x to exit. ')
        print('it is' if s==''.join(list(reversed(s))) else 'it isn\'t')
    else: 
        print('have a nice day!')
#lesson_six() 

# 7. create a list only containing even numbers of a random list
def lesson_seven(): 
    from random import randint
    l=[] 
    for i in range(0,randint(5,20)):
        l.append(randint(0,255))
    output=[] 
    for d in l: 
        if d%2==0: 
            output.append(d)
    # evenlist = [number for number in l if number % 2 == 0] 
    print(l) 
    print(output) 
#lesson_seven() 

# 8. rock paper scissors 
def lesson_eight(): 
    from random import randint
    print('let\'s play rock-paper-scissors. type r, p or s to play and anything else to exit')
    rps=({'r':'rock','p':'paper','s':'scissors'},{'p':'paper','s':'scissors','r':'rock'},{'s':'scissors','r':'rock','p':'paper'})
    while True: 
        #computer choice, index of rps-tuple 
        cc=randint(0,2) 
        cctuple=list(rps[cc].values())
        #user choice, decode input and detect index within computer selected tuple 
        ui=input('shoot! ')
        if ui not in('r','p','s'):
            print('have a nice day')
            break 
        uidecoded=rps[0][ui] 
        uc=cctuple.index(uidecoded)
        if uc<1: 
            finish='you lost, '+cctuple[1]+' beats '+uidecoded+'.'
        elif uc>1: 
            finish='you won, '+uidecoded+' beats '+cctuple[1]+'.'
        else: 
            finish='it\'s a draw.'
        print(finish) 
#lesson_eight() 

# 9. guess the random number until exit and count the guesses
def lesson_nine(): 
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
#lesson_nine() 

# 10. like 5 but only one line?
#see 5 

# 11. check if input number is prime or not
#see 4 

# 12. write a function to create a list from the first and last element of a given list
def lesson_twelve(): 
    from random import randint
    l=[randint(0,n) for n in range(0,randint(1,10))]
    nl=[] 
    nl.append(l[0]) 
    nl.append(l[-1]) 
    print(l) 
    print(nl) 
#lesson_twelve() 

# 13. fibonacci sequence 
def lesson_thirteen(): 
    while True: 
        ui=input('type in desired steps for fibonacci sequence, anything but integer to exit:')
        try: 
            ui=int(ui) 
        except ValueError: 
            print('have a nice day!')
            break 
        fibo=[0] 
        for i in range(0,ui):
            if fibo[i-1]: 
                fibo.append(fibo[i]+fibo[i-1]) 
            else: 
                fibo.append(1)
        print(fibo) 
#lesson_thirteen() 

# 14. remove duplicates from list
def lesson_fourteen(): 
    from random import randint
    l=[randint(0,n) for n in range(0,randint(10,25))]
    print(l) 
    nl=[] 
    for i in l: 
        if i not in nl: 
            nl.append(i) 
    print(nl) 
    nl2=list(set(l)) 
    print(nl2) 
#lesson_fourteen() 

# 15. reverse word order -> order word reverse 
def lesson_fifteen(): 
    ui=input('please type a sentence here: ')
    loop=ui.split(' ') 
    for i in reversed(loop):
        print(i+' ', end='')
#lesson_fifteen() 

# 16. random password generator with strong or weak passwords according to user request (first mix-case etc., latter one from a list of words)
def lesson_sixteen(): 
    import random 
    weak=('love','secret','sex','god')
    medium='abdcefghijklmnopqrstuvwxyz'
    strong='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.:-_!?()&' 
    choice=input('what kind of password do you want? weak, medium or strong? ')
    if choice=='weak': 
        password=weak[random.randint(0,len(weak)-1)]
    elif choice=='medium': 
        password=''.join(random.sample(medium,8))
    else: 
        temp=list(map(list, zip(random.sample(medium,8),random.sample(strong,8))))
        temp2=[''.join(a) for a in temp] 
        password=''.join(temp2)
    print(password) 
#lesson_sixteen() 

# 17. decode a webpage 


# 18. cows an bulls aka mastermind
def lesson_eighteen(): 
    from random import sample as rnd
    solution=rnd(range(0,9),4)
    guess=[] 
    guesses=0 
    while guess!=solution: 
        guess=input('type in four different numbers between 0 and 9, x to exit: ')
        if guess=='x': 
            print('have a nice day!')
            break 
        guess=[int(i) for i in guess] 
        guesses+=1 
        number=0 
        position=0 
        for x in solution: 
            if x in guess: 
                if guess.index(x)==solution.index(x):
                    position+=1
                else: 
                    number+=1
        if position: 
            print('1 number at right position' if position<2 else '%d numbers at right position' % position, end='. ')
        if number: 
            print('1 number correct' if number<2 else '%d numbers correct' % number, end='. ')
    else: 
        print('congratulations! it took you %d guesses.' % guesses)    
#lesson_eighteen() 

# 19. decode a webpage 2 


# 20. function to return boolean whether number is in ordered list or not
def lesson_twenty(): 
    def inlist(haystack, needle):
        return True if needle in haystack else False
    h=list(range(0,20)) 
    n=15 
    print(inlist(h,n)) 
#lesson_twenty() 

# 21. write to a file 
def lesson_twentyone(text='hello world!'):
    file=open('test.txt','w')
    file.write(text) 
    file.close() 
#lesson_twentyone('hello world into file...')

# 22. read from a file 
def lesson_twentytwo(): 
    file=open("test.txt","r")
    for line in file: 
        print(line) 
    file.close() 
#lesson_twentytwo() 

# 23. compare listed numbers within two files
def lesson_twentythree(): 
    from random import randint
    file1=open('list1.txt','w')
    file2=open('list2.txt','w')
    for i in range(0,randint(10,20)):
        a=str(randint(0,20+i))+'\n'
        b=str(randint(0,20+i))+'\n'
        file1.write(a) 
        file2.write(b) 

    file1.close() 
    file2.close() 
    file1=open('list1.txt','r')
    file2=open('list2.txt','r')

    list1=[] 
    for line in file1: 
        list1.append(line) 
    list2=[] 
    for line in file2: 
        list2.append(line) 

    file1.close() 
    file2.close() 

    print ('common: ',set(list1) & set(list2))    
    print ('unique: ',set(list1) | set(list2))    

#lesson_twentythree() 

# 24. print a game board with --- and | to the screen, with size according to user input
def lesson_twentyfour(board_x=[]): 
    # function prepared for later use in game
    import re 
    if not board_x: #prepared
        size=input('which size should the board have? type like 4x5: ')
        dim=size.split(re.findall(r'\D', size)[0]) 
        x,y=int(dim[0]),int(dim[1])
    else: # prepared 
        x,y=len(board_x[0]),len(board_x)
    for i in range(y*2+1): 
        for j in range(x): 
            if i%2: 
                print('| ',end='')
                print(board_x[i//2][j] if board_x else ' ',end='')  # prepared
                print(' ',end='')
            else: 
                print(' ---',end='') 
        print('|' if i%2 else '')
#lesson_twentyfour([[1,2,0],[1,0,2],[1,2,0]]) 
#lesson_twentyfour() 

# 25. guess the number reversed -> the programm has to find the number (user defines range)
def lesson_twentyfive(): 
    givenrange=int(input('think of a number and i try to guess it. please type in the maximum range to start: '))
    correct='' 
    tries=0 
    defrange=list(range(0,givenrange+1))
    while correct != '#': 
        if len(defrange)>1:
            guess=len(defrange)//2
            tries+=1 
            print('i guess number ',defrange[guess])
            correct=input('type + if my guess was too high, - if my guess was too low, # if i am right or if you want to quit: ')
            if correct=='+':
                defrange=[i for i in defrange if i<defrange[guess]]
            elif correct=='-': 
                defrange=[i for i in defrange if i>defrange[guess]]
        else: 
            print('then there\'s nothing left than ',defrange[0])
            correct='#' 
    else: 
        if tries<2: 
            print('whoa! seems to be my lucky day!')
        else: 
            print('it took me %d tries to guess your number.' % tries)
        print('have a nice day!')
#lesson_twentyfive() 

# 26. check for tic-tac-toe-winner with game like [[1,2,0],[1,0,2],[1,2,0]] 
def lesson_twentysix(board_x):
    # scalable to every size dependable of board_x list BUT winner can only be determined on square board at the moment
    lines=len(board_x) 
    columns=len(board_x[0])
    # rearrange entries to vertical
    board_y=[] # vertical 
    for y in range(0,columns):
        for x in range(0,lines):
            try: 
                 board_y[y]
            except: 
                board_y.append([])
            board_y[y].append(board_x[x][y]) 
    # rearrange entries to diagonal
    board_ul=[] # from upper left 
    board_ur=[] # from upper right 
    readxy=[[0]*lines] 
    readxy.append([]) 
    for i in range(columns):
        if i>0: 
            readxy[0].append(i)
        readxy[1].append(i)
    readxy[1].extend([columns-1]*(lines-1)) 
    #print('start coordinates: ',readxy)
    maxlen=lines if lines<=columns else columns
    for y in range(0,lines+columns-1): 
        for x in range(0,maxlen):
            try: 
                 board_ul[y]
            except: 
                board_ul.append([])
                board_ur.append([])
            uly=readxy[1][y]-x 
            ulx=readxy[0][y]+x 
            if uly<0: 
                continue 
            elif ulx>maxlen-1: 
                continue 
            else: 
                board_ul[y].append(board_x[uly][ulx]) 

            ury=readxy[0][y]+x 
            urx=readxy[0][-1-y]+x 
            if ury<0: 
                continue 
            elif urx>maxlen-1: 
                continue 
            else: 
                board_ur[y].append(board_x[ury][urx])         

    #print(board_x) 
    #print(board_y) 
    #print(board_ul) 
    #print(board_ur) 
    win1=[1]*maxlen 
    win2=[2]*maxlen 
    if win1 in board_x+board_y+board_ul+board_ur and win2 in board_x+board_y+board_ul+board_ur:
        return('draw') 
    elif win1 in board_x+board_y+board_ul+board_ur:
        return('player 1 wins')
    elif win2 in board_x+board_y+board_ul+board_ur:
        return('player 2 wins')
    else: 
        return False 

#print(lesson_twentysix([[1,2],[0,2],[1,2]])) 


# 27. input tic-tac-toe draw given coordinates starting at 1,1 (row/column) x and o alternating
class xinarow: 
    def __init__(self, x, y):
        self.board=[[0]*x for n in range(y)] 
    def draw(self, x, y, player):
        x,y=x-1,y-1 
        if self.board[y][x] == 0: 
            self.board[y][x]=player 
            return True 
        else: 
            return False 
    def free(self): 
        f=[] 
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]==0: 
                    f.append([i,j])
        return f 
                 
def lesson_twentyseven(): 
    game=xinarow(3,3) 
    print(game.board) 
    game.draw(1,1,2) 
    print(game.board) 
    if game.draw(3,3,1): 
        print(game.board) 
#lesson_twentyseven() 

# 28. return the largest of three given numbers only by using variables and if statements
def lesson_twentyeight(): 
    import re 
    ui=input('give tree separated numbers, please: ')
    dim=ui.split(re.findall(r'\D', ui)[0]) 
    x,y,z=int(dim[0]),int(dim[1]),int(dim[2])
    if z>x: 
        x,z=z,x 
    if y>x: 
        x,y=y,x 
    print('%d is the largest number'%x)
#lesson_twentyeight() 
     
# 29. working tic-tac-toe 
def lesson_twentynine(): 
    import re 
    brd=input('play a game of x-in-a-row. tell me about the board dimensions (e.g. 3x3): ')
    dim=brd.split(re.findall(r'\D', brd)[0]) 
    x,y=int(dim[0]),int(dim[1])
    # atm only sqare games are supported
    if x!=y: 
        y=x 
        print('only sqare games are supported at the moment. board has been adjusted to %dx%d'%(x,y)) 
    game=xinarow(x,y) 
    opponent=input('do you want to play against me or a friend? type \'a\' for pc match or \'b\' for human match: ')
    print('ok, let\'s begin!')
    if opponent!='b': 
        import random 
    while len(game.free())>1:
        player1=input('player 1, please type in x-y coordinates for your draw: ')
        p1=player1.split(re.findall(r'\D', player1)[0]) 
        if not game.draw(int(p1[0]),int(p1[1]),1):
            print('field already set.')
            continue 
         
        if len(game.free()):
            if opponent=='b':
                fault=True 
                while fault:
                    player2=input('player 2, please type in x-y coordinates for your draw: ')
                    p2=player2.split(re.findall(r'\D', player2)[0]) 
                    if not game.draw(int(p2[0]),int(p2[1]),2):
                        print('field already set.')
                    else: 
                        fault=False
            else: 
                field=random.sample(game.free(),1)
                #why is field unsubscriptable according to vsCode? it works though...
                game.draw(int(field[0][1])+1,int(field[0][0])+1,2) 
         
        # print current game
        lesson_twentyfour(game.board)
        # evaluate winner 
        if lesson_twentysix(game.board):
            print(lesson_twentysix(game.board))
            break 
         
#lesson_twentynine() 

# 30. hangman picking word from a list of words in external file
def lesson_thirty(): 
	import re
	from random import randint
	file=open("test.txt","r")
	wordlist=re.split(r"\W+",file.readlines()[0]) 
	file.close()
	sol=''
	while sol=='':
		sol=wordlist[randint(0,len(wordlist)-1)]
	return sol
#print(lesson_thirty())

# 31. guess letters (hangman with infinite guesses)
# 32. working hangman
def lesson_thirtytwo():
	sol=lesson_thirty()
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
#lesson_thirtytwo()

# 33. return some persons birthday from dictionary given name from user input
def lesson_thirtythree():
	dictionary={'anne':'09.05.2011','luke':'31.07.2013','tony':'24.10.2016'}
	print('ask for birthdate of following persons:')
	for key, value in dictionary.items():
		print(key)
	sel=input('who? ')
	print('{} has birthday on {}'.format(sel,dictionary[sel]))
#lesson_thirtythree()

# 34. return some persons birthday (see 33) from external json file, add to the file if new data is put in
import json
class handlejson():
	def __init__(self,value):
		self.file=value
	def read(self):
		with open(self.file,"r") as fr:
			try:
				data=json.load(fr)
			except:
				data={}
		return data
	def write(self,data):
		with open(self.file,'w') as fp:
			json.dump(data,fp)
		
def lesson_thirtyfour():
	instance=handlejson('json.json')
	data=instance.read()
	if len(data)==0:
		print('no data available. add one?')
	look=str(input('who\'s birthday? '))
	try:
		find=data[look]
		print('{} has birthday on {}'.format(look,find))
	except:
		new=str(input('{} not found. type in birthday as dd.mm.yyyy to append: '.format(look)))
		import re
		if re.match(r"\d\d\.\d\d\.\d\d\d\d",new):
			data[look]=new
			instance.write(data)
			print('{} added'.format(look))
		else:
			print('no date typed.')
#lesson_thirtyfour()

# 35. count how many persons in json file (see 34) have birthday within the months 
def lesson_thirtyfive():
	instance=handlejson('json.json')
	all=instance.read()
	import calendar
	year={}
	for i,j in all.items():
		month=calendar.month_name[int(j[3:5])]
		try:
			year[month]+=1
		except:
			year[month]=1
	for i,j in year.items():
		print('in {} there are {} birthdays'.format(i,j))
	
lesson_thirtyfive()

#p 36. plot a graphical output of 35




