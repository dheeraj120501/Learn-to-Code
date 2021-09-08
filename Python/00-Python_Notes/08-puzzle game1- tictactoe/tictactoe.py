#TicTacToe
EMPTY = '[ ]'
def display_board(board):
    for row in board:
        print()  # change the line
        for col in row:
            print(col, end='')
    print()

def is_full(board):
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True

def register_move(board, r, c, symbol):
    if r >= 0 and r <=2: # a valid row
        if c >=0 and c <=2: # a valid col
            if board[r][c] == EMPTY: # an empty cell
                board[r][c] = symbol#upate
                return True
    return False

def wins(board, symbol):
    #diagonal
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True #wins

    #reverse diagonal
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True #wins

    #horizontal
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True #wins

    #vertical
    for i in range(3):
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True #wins

    return False #not won

def tictactoe():
    #board:
    row1 = [EMPTY, EMPTY, EMPTY]
    row2 = [EMPTY, EMPTY, EMPTY]
    row3 = [EMPTY, EMPTY, EMPTY]
    board = [row1, row2, row3]

    #players
    players = []
    for i in range(1,3):
        print('Enter name for Player', i, ' ')
        players.append(input())

    #symbols
    symbols = ['[O]', '[X]'] #preset

    #Render the player(symbol) information
    for i in range(2):
        print('Player : ', players[i],  symbols[i] )

    #Game
    print('Lets Play !!!')
    current_player = 0 #preset
    is_draw = True #preset
    while not is_full(board):
        display_board(board)
        print(players[current_player], symbols[current_player], 'plays')
        r = int(input('Enter Row(0-2) '))
        c = int(input('Enter Col(0-2) '))
        if register_move(board, r, c, symbols[current_player]):
            display_board(board)
            #valid move, check for win
            if wins(board, symbols[current_player]):
                print(players[current_player], symbols[current_player], 'WINS !!!')
                is_draw = False
                break
            current_player = (current_player+1) % 2 #changing the player
        else:
            print('Invalid Move :( ')

    if is_draw:
        print('Well played by ', players[0] ,'and', players[1])
        print('Game Draw!!!')

def main():
    tictactoe()

main()