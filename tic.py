test_board=[" "]*9


def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


players_turn='x'


def players_position():
  
    global players_turn
    global test_board

    display_board(test_board)
    turns = 0
    
    while turns < 9:
        position=int(input(players_turn + ' enter you position:'))

        if test_board[position]==" ":
            test_board[position] = players_turn
            display_board(test_board)
            turns += 1
        else:
            print('this position is already taken \n Move to which place')
            display_board(test_board)

            continue

        if players_turn == 'x':
            players_turn ='o'
        else:
            players_turn = 'x'
        

players_position()



def win_check(board):
    global players_turn
    while True:
        if board[6]== board[7] and board[7]== board[8] and board[8] ==board[6] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break
            
        elif board[0] == board[1] and board[1] == board[2] and board[2] == board[1] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break

        elif board[3] == board[4] and board[4] == board[5] and board[5] == board[6] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break

        elif board[0] == board[3] and board[3] == board[6] and board[6] == board[0] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break

        elif board[1] == board[4] and board[4] == board[7] and board[7] == board[1] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break

        elif board[2] == board[5] and board[5] == board[8] and board[8] == board[2] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break

        elif board[0] == board[4] and board[4] == board[8] and board[8] == board[0] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break

        elif board[2] == board[4] and board[4] == board[6] and board[6] == board[2] != ' ':
            print('\n Game over')
            print('\n {} wins'.format(players_turn))
            break

        
win_check(test_board)


        
