from os import system
from time import sleep
from random import randint

# welcome message
print('Welcome to our simple tictactoe implementation\n' +
      'would you like to play ?\n' +
      '[Player name/No]: ', end='')

# read user reply
isRight = name = None
while len(name:= input()) < 2:
    print('this is an invalid response, plz try again')

# if he dont want to to play then Bye Bye
if name.lower() in {'no', 'nope'}:
    print('bye bye, have a nice day :)')
    exit()

# ok he wanna play lets define the board
board = [[None for i in range(3)] for j in range(3)]
def playAt(x,y,player):
    if(board[x][y] == None):
        board[x][y] = player['sign']
        print('"%s" marked an "%s" at (X:%d, Y:%d)'
        % (player['name'], player['sign'], x+1,y+1) )

    else:
        print('sorry this is already marked')
        turnof(player)

# define players and their decisions
def compute(): # play readin randomly
    print('thinking...')
    sleep(3)
    return randint(1, 9)

players = [
    {'name': name, 'sign': 'X', 'choose': input},
    {'name': 'computer', 'sign': 'O', 'choose': compute},
]

# who's gonna win
def win(board): #TODO: dtermine the winner
    return False

# start players turns
def turnof(player):
    def showBoard(board):
        print('')
        for rid,row in enumerate(board):
            row = [
                (str(3*rid+iid+1) if item == None else item)
                for iid, item in enumerate(row)
                ]
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
    turnof(players[whoPlay])

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
