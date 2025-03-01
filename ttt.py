
import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    if " " not in board:
        return "Tie"
    return False

def minimax(board, depth, is_maximizing):
    result = check_win(board)
    if result:
        if result == "X":
            return -10 + depth
        elif result == "O":
            return 10 - depth
        elif result == "Tie":
            return 0

    if is_maximizing:
        best_score = -1000
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -1000
    best_move = 0
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def game():
    board = [" "] * 9
    while True:
        print_board(board)
        move = input("Enter your move (1-9): ")
        if board[int(move) - 1] != " ":
            print("Invalid move, try again.")
            continue
        board[int(move) - 1] = "X"
        result = check_win(board)
        if result:
            print_board(board)
            if result == "X":
                print("You win!")
            elif result == "O":
                print("AI wins!")
            else:
                print("It's a tie!")
            break
        ai_move_index = ai_move(board)
        board[ai_move_index] = "O"
        result = check_win(board)
        if result:
            print_board(board)
            if result == "X":
                print("You win!")
            elif result == "O":
                print("AI wins!")
            else:
                print("It's a tie!")
            break

game()


