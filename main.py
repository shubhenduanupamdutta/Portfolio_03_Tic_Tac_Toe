import os
import numpy as np
import random

GAME_TITLE = """
888   d8b        888                   888                    
888   Y8P        888                   888                    
888              888                   888                    
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
888   888888     888   .d888888888     888   888  88888888888 
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888  
"""

board = np.array([[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]])


def print_board():
    current_board = f"""
      | A | B | C |
    ---------------
    1 | {board[0, 0]} | {board[0, 1]} | {board[0, 2]} |
    ---------------
    2 | {board[1, 0]} | {board[1, 1]} | {board[1, 2]} |
    ---------------
    3 | {board[2, 0]} | {board[2, 1]} | {board[2, 2]} |                     
    """
    print(current_board)


# Present the Game
header = f"""
        {GAME_TITLE}

             YOU ARE PLAYING TIC TAC TOE
             
             PLAYER_1 PLAYS X 
             PLAYER_2 PLAYS O
             COMPUTER PLAYS O
             
     ENTER CELL CHOICES USING A1, B2, C1 AND SO ON...
------------------------------------------------------------------
******************************************************************
------------------------------------------------------------------ 
"""

cells_available = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]


def take_choice(player: str) -> str:
    while True:
        choice = input(f"{player} enter your cell choice: ")
        if choice.upper() in cells_available:
            cells_available.remove(choice.upper())
            return choice.upper()
        else:
            print("Choice is wrong, please try again!")


def update_board(cell: str, symbol: str):
    cell_map = {"A1": (0, 0), "B1": (0, 1), "C1": (0, 2),
                "A2": (1, 0), "B2": (1, 1), "C2": (1, 2),
                "A3": (2, 0), "B3": (2, 1), "C3": (2, 2)}
    row, col = cell_map[cell]
    board[row, col] = symbol


def check_array_same(ar: np.array) -> bool:
    """Checks if all element in the array are same, returns True, otherwise false"""
    return np.all(ar == ar[0])


def check_win_status() -> tuple[bool, str]:
    """Check if any one won, returns a boolean and the winning symbol"""
    possible_lines = [board[0], board[1], board[2], board[:, 0], board[:, 1], board[:, 2],
                      np.array([board[0, 0], board[1, 1], board[2, 2]]),
                      np.array([board[2, 0], board[1, 1], board[0, 2]])]

    someone_won, value = False, " "
    for line in possible_lines:
        if check_array_same(line) and line[0] != " ":
            value = line[0]
            return True, value
    return someone_won, value


def announce_winner(symbol: str):
    if symbol == "X":
        print("PLAYER_1 with symbol X is the winner. Congrats to PLAYER_1")
    elif symbol == "O" and not vs_computer:
        print("PLAYER_2 with symbol O is the winner. Congrats to PLAYER_2")
    else:
        print("COMPUTER with symbol O is the winner. PLAYER_1 loses!")


def win_or_draw() -> bool:
    any_win = check_win_status()
    if any_win[0]:
        announce_winner(any_win[1])
        return True
    if len(cells_available) == 0:
        print("No more move possible. Match is a draw.")
        return True


def play(player: str, symbol: str):
    if player == "COMPUTER":
        player_choice = random.choice(cells_available)
    else:
        player_choice = take_choice(player)
    update_board(player_choice, symbol)
    os.system("cls")
    print(header)
    print(f"{player} has played {player_choice}\n")
    print("Current status of the board is")
    print_board()


print(header)
print_board()

play_with_computer = input("Do you want to play with computer? (Y/N): ")
vs_computer = True if play_with_computer.upper() == "Y" else False
if vs_computer:
    print("\nYou chose to play with computer.\n")

match_decided = False
while not match_decided:
    play("PLAYER_1", "X")
    if win_or_draw():
        break

    if vs_computer:
        play("COMPUTER", "O")
    else:
        play("PLAYER_2", "O")
    if win_or_draw():
        break

print("\n")
