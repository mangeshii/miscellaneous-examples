test_board = [" "]*9


def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


players_turn = 'o'


def players_position():

    global players_turn
    global test_board

    display_board(test_board)
    turns = 0

    while turns < 9:
        position = int(input(players_turn + ' enter you position:'))

        if test_board[position] == " ":
            test_board[position] = players_turn
            display_board(test_board)
            turns += 1
        else:
            print('this position is already taken \n Move to which place')
            display_board(test_board)

            continue

        if players_turn == 'o':
            players_turn = 'x'
        else:
            players_turn = 'o'


players_position()



def win_check():
    if test_board[0] =='x' and test_board[1] == 'x' and test_board[2]=='x':
        print('x wins')
    elif test_board[0] == 'o' and test_board[1] == 'o' and test_board[2] == 'o':
        print('o wins')
   

win_check()
