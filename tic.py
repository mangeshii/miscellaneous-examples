board=[" "]*10


def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


players_turn='x'


def players_position():
    global players_turn
    global board
    display_board(board)
    turns = 0
    while turns < 9:
        position=int(input('player1 enter you position:'))

        board[position-1]=players_turn
        display_board(board)
        
        turns +=1

        if players_turn == 'x':
            players_turn ='o'
        else:
            players_turn = 'x'
players_position()


