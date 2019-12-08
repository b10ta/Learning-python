from os import system
from time import sleep
from random import randint

# welcome message
print('Welcome to our little game\n' +
      'would you like to play ?\n' +
      'if so, please introduce yourself\n'+
      'username: ', end='')

# read user reply
isRight = name = None
while len(name:= input()) < 2:
    print('try again plz')

# if he dont want to to play then Bye Bye
if name.lower() in ['no', 'nope']:
    print('bye bye, have a nice day :)')
    exit()

# ok he wanna play lets define the board
board = [[None for i in range(3)] for j in range(3)]
def playAt(x,y,player):
    if(board[x][y] == None):
        board[x][y] = player['sign']
        print('"%s" filled the board at (X:%d, Y:%d)'
        % (player['sign'], x+1,y+1))
    else:
        print('sorry this one is already used')
        turnof(player)

# define players and their decisions
def compute():
    print('thinking...')
    sleep(3)
    return randint(1, 9)

players = [
    {'name': 'computer', 'sign': 'x', 'choose': compute},
    {'name': name, 'sign': 'o', 'choose': input},
]

# who's gonna win
def win(board):
    return False

# start players turns
def turnof(player):
    def showBoard(board):
        print('')
        for row in board:
            row = map(lambda x: '#'if x == None else x, row)
            print('  | '+'  '.join(row)+' |')
            print('')
    system('clear')
    print('\n"%s" its your turn, plz choosea a decsion: ' % player['name'])
    showBoard(board)
    print(' < ', end='')
    colId = int(player['choose']())-1
    x = colId//3
    y = colId % 3
    playAt(x, y, player)

whoPlay = 0

while not(win(board)):
    # toggle turns
    whoPlay = int(not(whoPlay))
    turnof(whoPlay)

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

# still doing it
# not finished
# sorry :'(
# one min
# nice


# uhhh i am used to JS

# yeah yeah no semicolons
# wait there is no score on TicTac

# hmm... what is winning
# it's getting a full row of X
# or a full row of Y

# we cant on python???!!
# hmmm ok
# is there do-while in python?
# ok no simicolons ; hehe
# hehe lol not used to python