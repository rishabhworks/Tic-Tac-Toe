BOARD = ['0', '1', '2', '3', '4', '5', '6', '7', '8' ]

def print_board():
    print()
    print(BOARD[0] + ' | ' + BOARD[1] + ' | ' + BOARD[2])
    print('--+---+--')
    print(BOARD[3] + ' | ' + BOARD[4] + ' | ' + BOARD[5])
    print('--+---+--')
    print(BOARD[6] + ' | ' + BOARD[7] + ' | ' + BOARD[8])

def check_winner():
    for i in range(3):
        if BOARD[i] == BOARD[i+3] == BOARD[i+6]:
            return True
        if BOARD [ i * 3] == BOARD [ i * 3 + 1] == BOARD [ i * 3 + 2]:
            return True
    
    if BOARD[0] == BOARD[4] == BOARD[8]:
        return True
    
    if BOARD[2] == BOARD[4] == BOARD[6]:
        return True
    

    return False 
         
def make_move(move, cur_player):
    if BOARD[move] == 'X' or BOARD[move] == 'O':
        return False
    
    BOARD[move] = 'X' if cur_player == 1 else 'O'
    return True

def is_draw():
    for cell in BOARD:
        if cell != 'X' and cell != 'O':
            return False
    return True


    
    

