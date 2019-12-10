from os import system
from time import sleep
from random import randint

# say welcome to the player
print('Welcome to our simple Tic-Tac-Toe game\n would you like to play ?')

# the player take a decision to play or exit
name = input('[Player name/No]: ')
while len(name) < 1:
    name=input('invalid username, plz try again: ')

# exist if player dont like to play
if name.lower() in {'n', 'no', 'nope'}:
    print('bye bye, have a nice day :)')
    exit()

# if he wanna play, lets define the UI
def UiRender(ui): # render means draw
    system('clear')
    UI.update(ui)
    print('\n - %s\n\n' % UI['header'])
    for row in UI['board']:
        print('    [%s]    \n'%']  ['.join(row))
    print('\n%s' % UI['footer'], end='')
    
UI = { # the UI is what will the user see
	'header':'', 
	'board': [[str(3*y+x+1) for x in range(3)] for y in range(3)],
	'footer': '',
	'render': UiRender
}

# lets define how to fill the board
def playAt(x,y,player):
    if(UI['board'][x][y].lower() in {'x', 'y'}):
        UI['render']({'header':'this one is already played!'})
        sleep(.6)
        turnof(player)
        return
    UI['board'][x][y] = player['sign']
    UI['render']({'header':'"%s" played "%s" at (X:%d, Y:%d)'%(player['name'], player['sign'], x+1,y+1)})
    sleep(1.2)


# define players and their decisions
def compute(): # play readin randomly
    print('thinking...')
    sleep(2.7)
    return randint(1, 9)

players = [
    {'name': name, 'sign': 'X', 'choose': input},
    {'name': 'computer', 'sign': 'O', 'choose': compute},
]

# determine who's the winner, if there is any
def win(boardUi): #TODO: dtermine the winner
    return False

# start the turn of a certain player
def turnof(player):
    UI['render']({'header':'"%s" its your turn, plz choosea a decsion: ' % player['name'], 'footer':' < '})
    id = int(player['choose']())-1
    x, y = id // 3, id % 3
    playAt(x, y, player)

whoPlay = 0
while not(win(UI['board'])):
    # toggle turns
    turnof(players[whoPlay])
    whoPlay = int(not(whoPlay))
    


    # for row in board:
    #     s = 0
    #     init = row[0]
    #     if init == '':
    #         continue
    #     for col in row:
    #         if col != init:
    #             continue
    #         else:
    #             s += 1
    #     if s == 3:
    #         return init
