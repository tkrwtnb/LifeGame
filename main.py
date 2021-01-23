from icecream import ic
import time 
import os 
import random 

LINE_LEN = 30
SLEEP_TIME = 0.25

clear = lambda: os.system('clear')


def display_board(board):
    for line in board:
        for i, cell in enumerate(line):
            print(" ", end="")

            if i != LINE_LEN - 1:
                if not line[i]:
                    print("\u25A0", end="")
                else:
                    print(" ", end="")
            else:
                if not line[i]:
                    print("\u25A0")
                else:
                    print(" ")


def initialize_board(board):
    board.clear()

    for i in range(0, LINE_LEN):
        line = [True] * LINE_LEN
        rand_array = [random.randrange(LINE_LEN)] * 1000

        for random_index in rand_array:
            line[random_index] = False

        board.append(line)

    return board


def all_false_board(board):
    board.clear()

    for i in range(0, LINE_LEN):
        line = [False] * LINE_LEN
        board.append(line)

    return board


def calc_board(board):
    next_board = []
    for index in range(0, LINE_LEN):
        next_board.append([False] * LINE_LEN)

    for v, line in enumerate(board):
        for h, cell in enumerate(line):
            count = count_cell(v, h, board)
            if cell:
                if count != 2 and count != 3:
                    next_board[v][h] = False
                else:
                    next_board[v][h] = True
            else:
                if count == 3:
                    next_board[v][h] = True
                else:
                    next_board[v][h] = False

    return next_board


def count_cell(target_cell_v, target_cell_h, count_board):
    count = 0
    for v in range(target_cell_v - 1, target_cell_v + 2):
        for h in range(target_cell_h - 1, target_cell_h + 2):
            if 0 <= v < LINE_LEN and 0 <= h < LINE_LEN and not (v == target_cell_v and h == target_cell_h):
                if count_board[v][h]:
                    count = count + 1

    return count

def galaxy(v, h, board):
    for i in range(v, v + 2):
        for j in range(h, h + 6):
            board[v + i][h + j] = True

    for i in range(v, v + 6):
        for j in range(h + 7, h + 9):
            board[v + i][h + j] = True

    for i in range(v + 3, v + 9):
        for j in range(h, h + 2):
            board[v + i][h + j] = True

    for i in range(v + 7, v + 9):
        for j in range(h + 3, h + 9):
            board[v + i][h + j] = True

    return board

def grider(v, h, board):
    board[v][h + 1] = True
    board[v + 1][h + 2] = True
    board[v + 2][h + 0] = True
    board[v + 2][h + 1] = True
    board[v + 2][h + 2] = True
    
    return board


def blinker(v, h, board):
    board[v][h] = True
    board[v + 1][h] = True
    board[v + 2][h] = True

    return board


def main():
    # origin_board = initialize_board([])
    origin_board = all_false_board([])

    origin_board = grider(0, 0, origin_board)

    origin_board = galaxy(5, 5, origin_board)
    

    display_board(origin_board)


    while True:
        display_board(origin_board)

        origin_board = calc_board(origin_board)

        time.sleep(SLEEP_TIME)
        clear()


if __name__ == '__main__':
    main()
