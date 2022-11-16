from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

def print_board(board):
    print('  A B C D E F G H')
    print(' ==================')
    row_number = 1
    for row in board:
        print(f'{row_number}|'+'|'.join(row)+'|')
        row_number += 1

letters_to_numbers = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def board():
    pass

def create_ships(board):
    for ship in range(5):
        ship_row = randint(0,7)
        ship_column = randint(0,7)
        while board[ship_row][ship_column] == 'x':
            ship_row,ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'x'

def guess_location():
    row = input(f'Please enter a row from 1 to 8: ')
    while str(row) not in '12345678':
        print('Please enter a valid row')
        row = (input(f'Please enter a row from 1 to 8: '))
    
    column = input(f'Please enter a column from A to H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input(f'Please enter a column from A to H: ').upper()
    
    if HIDDEN_BOARD[int(row) - 1][letters_to_numbers[column]] == 'x':
        print('Hit! You sunk a battleship!')
        GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] = 'x'
        print_board(GUESS_BOARD)
    elif HIDDEN_BOARD[int(row) - 1][letters_to_numbers[column]] == '-':
        print('You cannot target the same location more than once.\n please choose again.')
        guess_location()
    else:
        print('Miss. There is no battleship at this location.')
        GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] = '-'
        print_board(GUESS_BOARD)

def count_hit_ships():
    pass

create_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)
print_board(GUESS_BOARD)
guess_location()