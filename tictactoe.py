import numpy as np


def main():
    board = np.empty((3, 3), dtype=str)
    board_key = np.arange(1, 10, 1).reshape(3, 3)
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

    icon = input("Do you want to be Xs or Os?")

    while not (icon.lower() == "x" or icon.lower() == "o"):
        print("Choose a valid icon!")
        icon = input("Do you want to be Xs or Os?")

    while isPlaying == True:
        display_key(board_key)
        user_move(board_key, icon)


def exit_game():
    print("Thank you for playing!")
    exit()


def cpu_move():

    return


def user_move(board_key, icon):
    pos = input("Select a cell by picking a number from the board: \n")
    for x in board_key:
        while x == pos:
            x = input("That spot is taken! Pick a different move.")
    move = board_key.index(pos)
    board_key[move] = icon


def display_key(board_key):
    print(board_key)


main()
