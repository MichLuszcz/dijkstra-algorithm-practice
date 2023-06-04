from argparse import ArgumentParser
from CellClass import Cell


def prep_parser() -> str:
    parser = ArgumentParser()
    args = parser.parse_args()
    parser.add_argument("filename", help="Name of a file to read")

    return args.filename


def read_board() -> list:
    filename = prep_parser()
    board = []
    len_of_row = 0
    diff = 0
    with open(filename, 'r') as file_handle:
        for index, line in enumerate(file_handle):
            board.append(list(line.rstrip('\n')))
            if len(line.rstrip('\n')) < len_of_row:
                diff = len_of_row - len(line.rstrip('\n'))
                for _ in range(diff):
                    board[index].append(' ')
            len_of_row = len(board[index])

    return board


def number_to_object_grid(number_grid: list) -> list:
    object_grid = []
    row_index = 0
    for row in number_grid:
        object_row = []
        column_index = 0
        for element in row:
            if element.isnumeric():
                object_row.append(Cell(float('inf'), True, [column_index, row_index], element))
            elif element == 'X' or element == 'x':
                object_row.append(Cell(float('inf'), True, [column_index, row_index], 0))
            else:
                # spacja
                object_row.append(Cell(float('inf'), False, [column_index, row_index], 0))
            column_index += 1
        object_grid.append(object_row)
        row_index += 1
    return object_grid


def test():
    board = read_board()
    for row in board:
        print(row)
    obj_board = number_to_object_grid(board)
    for row in obj_board:
        print(row)

test()
