from board import print_board, make_move , check_winner,  is_draw 
import random

cur_player = 1
PLAYER_NAME = ''

def start():
    PLAYER_NAME = input('Enter your Name: ')
    print_board()
    while not check_winner():
        if is_draw():
            print("it's s draw!")
        if cur_player == 1:
            player_move()
        else:
            computer_move()
        print_board()
        switch_player()
    print(f'{PLAYER_NAME} wins!' if cur_player == 2 else 'Computer wins!')


def player_move():
    move = int(input('Enter cell number to make a move: '))
    is_valid_move = make_move(move, cur_player)
    while not is_valid_move:
        print('Invalid Move!')
        move = int(input('Enter cell number to make a move: '))
        is_valid_move = make_move(move, cur_player)

def computer_move():
    print("Computer's move.....")
    move = random.randint(0,8)
    is_valid_move = make_move(move, cur_player)
    while not is_valid_move:
        move = random.randint(0,8)
        is_valid_move = make_move(move, cur_player)

def switch_player():
    global cur_player
    cur_player = 2 if cur_player == 1 else 1


