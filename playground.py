from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]
turns = 20

def increment_turns():
    global turns
    turns -= 1
    print(f'Turns remaining: {turns}')

def print_board(board):
    print('  A B C D E F G H')
    print(' ==================')
    row_number = 1
    for row in board:
        print(f'{row_number}|'+'|'.join(row)+'|')
        row_number += 1

letters_to_numbers = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

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
        row = input(f'Please enter a row from 1 to 8: ')
    
    column = input(f'Please enter a column from A to H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input(f'Please enter a column from A to H: ').upper()

    return (row,column)

def check_guess(row,column):
    try:
        if GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] == '-' or GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] == 'x':
            print('\n You cannot target the same location more than once.\n please choose again.')
            guess_location()

        elif HIDDEN_BOARD[int(row) - 1][letters_to_numbers[column]] == 'x':
            print('\n Hit! You sunk a battleship!')
            GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] = 'x'
            increment_turns()
            print_board(GUESS_BOARD)

        else:
            print(f'\n Miss. There is no battleship at this location.{row}{column}')
            GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] = '-'
            increment_turns()
            print_board(GUESS_BOARD)
    except ValueError:
        print('Please add a valid target location')
        guess_location()
    except KeyError:
        print('Please add both a valid row AND column')
        guess_location()

def count_hit_ships(board):
    count = 0
    for row in board:
        for cell in row:
            if cell == 'x':
                count += 1
    return count


def main():
    print('Welcome to battleships')
    print(f'You have {turns} to sink all 5 ships.')
    create_ships(HIDDEN_BOARD)
    print_board(HIDDEN_BOARD)
    print_board(GUESS_BOARD)
    while turns > 0:
        guess_row,guess_column = guess_location()
        check_guess(guess_row,guess_column)
        if count_hit_ships(GUESS_BOARD) >= 5:
            print ('\nYou hit all battleships. You win!')
            break
        elif turns == 0:
            print('\nGame Over, you ran out of turns')
            print('Ship Locations')
            print_board(HIDDEN_BOARD)
            break

main()
