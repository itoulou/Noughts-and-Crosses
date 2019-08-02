def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("______")
    print("")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("______")
    print("")
    print(board[1] + '|' + board[2] + '|' + board[3])

def check_win(board, marker):
    if board[7] == board[8] == board[9] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[1] == board[2] == board[3] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True    
    elif board[3] == board[6] == board[9] == marker:
        return True
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[7] == board[5] == board[3] == marker:
        return True 
    else:
        return False   

def play(player_1, player_2):
    board = [" "] * 10
    display_board(board)
    print("Player 1 has first go\nPick a number between 1-9")
    turns = 1
    
    while(turns < len(board)):
        player_number = int(input(" "))
        
        

        if player_number > 0 and player_number < 10  and board[player_number] == " " and turns % 2 != 0:
            board[player_number] = player_1
            display_board(board)
            if check_win(board, player_1):
                print("Player 1 wins")
                return True
            turns += 1
        elif player_number > 0 and player_number < 10  and board[player_number] == " " and turns % 2 == 0:
            board[player_number] =  player_2
            display_board(board)
            if check_win(board, player_2):
                print("Player 2 wins")
                return True
            turns += 1
        elif board[player_number] != " ":
            print("Square has already been used, please pick a free a square")    
        else:
            print("Please enter a number between 1-9") 

def main():


    flag = True
    while(flag):
        
        player_1 = input("Do you want to be X or O: ")
        if player_1.upper() == 'X':
            player_2 = 'O'
            print("Player 1 is X")
            print("Player 2 is O")
            
        else:
            player_2 = 'X'
            player_1 = 'O' 
            print("Player 1 is O")
            print("Player 2 is X")

        ready = input("Are you ready to play?: Yes/No: ")
        if ready.lower() != 'yes':
            print("Exiting game...")
            flag = False
        else:
            finished = play(player_1, player_2)
            if finished == True:
                flag = False
      

    replay = input("Play again?, Yes/No: ")
    if replay.lower() == "yes":
        main()
    else:
        print("Exiting game...")    
    
         


main()

