from icecream import ic
import time 
import os 
import random 
LINE_LEN = 50

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
        line = [False] * LINE_LEN
        rand_array = [random.randrange(LINE_LEN)] * 1000

        for random_index in rand_array:
            line[random_index] = True

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

def main():
    origin_board = initialize_board([])

    display_board(origin_board)

    # blinker
    origin_board[0][1] = True
    origin_board[1][1] = True
    origin_board[2][1] = True


    while True:
        display_board(origin_board)

        origin_board = calc_board(origin_board)

        time.sleep(0.5)
        clear()


if __name__ == '__main__':
    main()
