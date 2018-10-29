"""
this is a practice of classes, their properties, functions and loops. and a brilliant story development.
"""
from random import randint
import sys

class character():
    def __init__(self,value):
        self.type=value['type']
        self.name=value['name']
        self.health=value['health']
        self.restaurators=value['restaurators']
    def hit(self):
        if self.health>0:
            self.health-=randint(0,20)
    def inspect(self):
        return '%s is a %s with a health of %d and carries %d restaurators.'%(self.name,self.type,self.health,self.restaurators)

def help():
    text="""type your command.
[inspect character_name] gives you the information about the character. type [inspect myself] to obtain information about your status
[fight character_name] fights a character, but be aware the character fights back! you retrieve items from the deceased
[heal character_name] restores health unless you are out of restaurators. to heal yourself type [heal myself]
[lookaround] tells you who is around
[quit] exits the program

fights and healings affect the health randomly. if you die, the program quits.
"""
    print(text)

def quit():
    print('goodbye...')
    sys.exit()

def lookaround():
    global characters
    print('you look around and see')
    for names in characters:
        print(characters[names].inspect())

def inspect(whom):
    print(whom.inspect())

def heal(whom):
    global characters
    if characters['myself'].restaurators>0:
        whom.health+=randint(10,20)
        characters['myself'].restaurators-=1
        print('your healing has left you with %d restaurators'%characters['myself'].restaurators)
    else:
        print('as you have no restaurators left you can not heal anyone')

def fight(opponent):
    global characters
    opponent.hit()
    if opponent.health>0:
        characters['myself'].hit()
    else:
        characters['myself'].restaurators+=opponent.restaurators
        print('%s has ceased to exist'%(opponent.name))
        del characters[opponent.name]
    if characters['myself'].health<1:
        print('you\'ve ceased to exist.')
        quit()

def act():
    handleCharacters={  'heal':heal,
                        'fight':fight,
                        'inspect':inspect
    }
    commands={  'help':help,
                'quit':quit,
                'lookaround':lookaround
    }
    while True:
        action=input(': ').split()
        if action[0] in handleCharacters.keys():
            try:
                handleCharacters[action[0]](characters[action[1]])
            except:
                print('command not found')
        else:
            try:
                commands[action[0]]()
            except Exception as e:
                print('command not found',e)

characters={}

playername, playertype= 'ironfist','good guy' # input('enter your name: '), input('enter your type of character: ')
characters['myself']=character({'type':playertype,'name':playername+' (you)','health':randint(20,40),'restaurators':3})
print('hello %s, so you start as a %s, with a health value of %d. if you don\'t know what to to type [help].'%(characters['myself'].name,characters['myself'].type,characters['myself'].health))

characters['scarface']=character({'type':'bad guy','name':'scarface','health':randint(20,40),'restaurators':randint(0,3)})
print('\nyou see %s. %s'%(characters['scarface'].name,characters['scarface'].inspect()))

if __name__=='__main__':
    act()