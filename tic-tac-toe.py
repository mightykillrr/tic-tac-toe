# TicTacToe game built in Python by Aniket Kotal

import random
from time import sleep


def display_board(board):
    print("\n"*100)
    print("Current Board: ")
    print("  " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print(" ---+---+--- ")
    print("  " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print(" ---+---+--- ")
    print("  " + board[1] + " | " + board[2] + " | " + board[3] + "  ")


def choose_marker():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Please choose X or O: ").upper()
        if marker == 'X':
            return 'X', 'O'
        elif marker == 'O':
            return 'O', 'X'
        else:
            print("Either 'X' or 'O', Dummy!")


def player_input(board, marker, pos):
    board[pos] = marker


def emptyspace_check(board, pos):
    return board[pos] == ' '


def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


def first_move():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def board_if_filled(board):
    for i in range(1, 10):
        if emptyspace_check(board, i):
            return False
    return True


def playerchoice(board, chance, marker):
    pos = 0
    if chance == "Player 1":
        while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not emptyspace_check(board, pos):
            try:
                print(" ")
                pos = int(input(f"Player 1({marker}), Please enter where to place your marker(1-9): "))
            except ValueError:
                print("Invalid input!")
        return pos
    elif chance == "Player 2":
        while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not emptyspace_check(board, pos):
            try:
                print(" ")
                pos = int(input(f"Player 2({marker}), Please enter where to place your marker(1-9): "))
            except ValueError:
                print("Invalid input!")
        return pos


def playagain():
    response = ""
    while response not in ['YES', "Y", 'NO', 'N']:
        response = input("Do you want to play again? ").upper()
        if response in ['YES', "Y"]:
            print("Yay! Let's get the game set up for you shall we!")
            return True
        elif response in ['NO', 'N']:
            print("Awe ;(")
            return False
        else:
            print("Yes or No?")
            response = " "


def number_view():
    print("  7 | 8 | 9  ")
    print(" ---+---+--- ")
    print("  4 | 5 | 6  ")
    print(" ---+---+--- ")
    print("  1 | 2 | 3  ")


# main code
print(" ")
print("Welcome to my TicTacToe game!")
while True:
    mainboard = [" "] * 10
    p1_marker, p2_marker = choose_marker()
    turn = first_move()
    print("Please wait while we selecting who goes first.")
    sleep(.5)
    print(turn + " goes first!")

    game = ""
    gameplay = ""
    while game not in ['YES', 'Y'] and game not in ["NO", "N"]:
        print(" ")
        game = input("Are you ready to begin? ").upper()
        if game in ["YES", "Y"]:
            gameplay = True
        elif game in ["NO", "N"]:
            gameplay = False
        else:
            print("Yes or No?")

    while gameplay:
        if turn == "Player 1":
            display_board(mainboard)
            print("The places are filled with the number input from 1-9 in the following manner:")
            number_view()
            position = playerchoice(mainboard, turn, p1_marker)
            player_input(mainboard, p1_marker, position)

            if win_check(mainboard, p1_marker):
                display_board(mainboard)
                print("+------------------+")
                print("|Player 1 has won! |")
                print("+------------------+")
                sleep(3)
                gameplay = False
            else:
                if board_if_filled(mainboard):
                    display_board(mainboard)
                    print("+------------------+")
                    print("|It's a Tie!       |")
                    print("+------------------+")
                    sleep(3)
                    break
                else:
                    turn = "Player 2"
        if turn == "Player 2":
            display_board(mainboard)
            print("The places are filled with the number input from 1-9 in the following manner:")
            number_view()
            position = playerchoice(mainboard, turn, p2_marker)
            player_input(mainboard, p2_marker, position)

            if win_check(mainboard, p2_marker):
                display_board(mainboard)
                print("+------------------+")
                print("|Player 2 has won! |")
                print("+------------------+")
                sleep(3)
                gameplay = False
            else:
                if board_if_filled(mainboard):
                    display_board(mainboard)
                    print("+------------------+")
                    print("|It's a Tie!       |")
                    print("+------------------+")
                    sleep(3)
                    break
                else:
                    turn = "Player 1"
    if not playagain():
        print(" ")
        print("+-------------------------------------------------------------------+")
        print("|Thanks for using this app! Hit me up on Discord: mightykiller#9119 |")
        print("+-------------------------------------------------------------------+")
        sleep(4)
        break
