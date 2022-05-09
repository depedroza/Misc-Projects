import numpy as np
import random


def main():
    board = np.full((3, 3), "-")

    isPlaying = False

    print(board)
    i = input("Welcome to TicTacToe! Ready to Start?: ")
    if i.lower().startswith("n"):
        exit_game()

    elif i.lower().startswith("y"):
        isPlaying = True

    while not (i.lower().startswith("y") or i.lower().startswith("n")):
        i = input("Please indicate 'yes' or 'no'")
        if i.lower().startswith("n"):
            exit_game()

        elif i.lower().startswith("y"):
            isPlaying = True

    icon = input("Do you want to be Xs or Os?").upper()

    while not (icon.lower() == "x" or icon.lower() == "o"):
        print("Choose a valid icon!")
        icon = input("Do you want to be Xs or Os?")

    play_game(isPlaying, icon)


def play_game(isPlaying, icon):
    board = np.full((3, 3), "-")
    openslots = 9
    display_board(board)
    while isPlaying == True:
        board = user_move(board, icon)
        openslots -= 1
        display_board(board)
        check_winner(board, icon, openslots)
        print("The CPU moves!")
        board = cpu_move(board, icon)
        openslots -= 1
        display_board(board)
        check_winner(board, icon, openslots)


def exit_game():
    print("Thank you for playing!")
    exit()


def cpu_move(board, icon):
    good_move = False
    if icon.lower() == "x":
        cpu_icon = "O"
    else:
        cpu_icon = "X"
    while good_move == False:
        column = random.randint(1, 3)
        row = random.randint(1, 3)
        if board[row - 1, column - 1] == "-":
            board[row - 1, column - 1] = cpu_icon
            good_move = True
    return board


def user_move(board, icon):
    good_move = False
    while good_move == False:
        row = input("Select a row to place your move (1-3): \n")
        row = int(row)
        column = input("Select a column to place your move (1-3). \n")
        column = int(column)
        if (row < 4) and (column < 4):
            if board[row - 1, column - 1] == "-":
                board[row - 1, column - 1] = icon
                good_move = True
            else:
                print("Choose an empty space!")
        else:
            print("Choose a Row and Column from 1-3!")
    return board


def display_board(board):
    print(board)


def check_winner(board, icon, openslots):
    if icon.lower() == "x":
        cpu_icon = "O"
    else:
        cpu_icon = "X"

    for i in range(0, 3):
        rows_win = (board[i, :] == icon).all()
        cols_win = (board[:, i] == icon).all()
        if rows_win or cols_win:
            print("******* YOU WIN *******")
            exit_game()
        rows_win = (board[i, :] == cpu_icon).all()
        cols_win = (board[:, i] == cpu_icon).all()
        if rows_win or cols_win:
            print("Loser!")
            exit_game()

    diag_win1 = (np.diag(board) == icon).all()
    diag_win2 = (np.diag(np.fliplr(board)) == icon).all()

    if diag_win1 or diag_win2:
        print("******* YOU WIN *******")
        exit_game()
    diag_win1 = (np.diag(board) == cpu_icon).all()
    diag_win2 = (np.diag(np.fliplr(board)) == cpu_icon).all()

    if openslots == 0:
        print("DRAW")
        exit_game()


main()
