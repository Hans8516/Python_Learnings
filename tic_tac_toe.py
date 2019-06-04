'''Tic tac toe for 2 users in python'''
#TODO(hans8516) add invalid input checks

def display_board(boarditems):
    print (boarditems[1] + '|' + boarditems[2] + '|' + boarditems[3])
    print ("-" + '|' + "-" + '|' + '-')
    print (boarditems[4] + '|' + boarditems[5] + '|' + boarditems[6])
    print ("-" + '|' + "-" + '|' + '-')
    print (boarditems[7] + '|' + boarditems[8] + '|' + boarditems[9])

display_board(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


def get_input(user,boarditems, position, mark):
    if user==1:
        boarditems[position] = mark
    else:
        boarditems[position] = mark
    display_board(boarditems)
    return boarditems

def check_if_winner(mark, board):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def get_user_symbol():
    symbol=input('User1 enter your choice "X" or "O" :')
    return symbol.upper()
def is_draw(boarditems):
    for  i in range(1,10):
        if boarditems[i]==' ':
            return False
    return True        
    
def game():
    boarditems = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    wanna_play = input('Do you want to play tic tac toe : [y/n] :')
    if wanna_play == 'y' or wanna_play == 'Y':
        user1_symbol= get_user_symbol()
        if user1_symbol=='X':
            user2_symbol='O'
        else:
            user2_symbol='X'
        
        user=1
        winner = False
        while not winner:
            expecting_correct_input=True
            if user%2==0:
                
                position=input('User2 Enter the position where you want to put your symbol:')
                position = int(position)
                if boarditems[position] is not ' ':
                    expecting_correct_input = False
                if expecting_correct_input:
                    boarditems = get_input(user,boarditems,int(position),user2_symbol)
                    winner = check_if_winner(user2_symbol,boarditems)
                    if winner:
                        print ('User {} has won the game'.format(user))
            else :
                position = input('User1 Enter the position where you want to put your symbol:')
                position = int(position)
                if boarditems[position] is not ' ':
                    expecting_correct_input = False
                
                if expecting_correct_input:
                    boarditems = get_input(user, boarditems, int(position), user1_symbol)
                    winner = check_if_winner(user1_symbol, boarditems)
                    if winner:
                        print ('User {} has won the game'.format(user))
            if is_draw(boarditems):
                print ("Game Draw! Thank You")
                break
            if expecting_correct_input:
                user = (user+1)%2
            expecting_correct_input = True
            

game()
