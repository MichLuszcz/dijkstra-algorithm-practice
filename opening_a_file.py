from argparse import ArgumentParser
from CellClass import Cell


def prep_parser() -> str:
    parser = ArgumentParser()
    parser.add_argument("filename", help="Name of a file to read")
    args = parser.parse_args()
    return args.filename


def read_board() -> list:
    filename = prep_parser()
    board = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            board.append(list(line.strip()))

    return board


def number_to_object_grid(number_grid: list) -> list:
    object_grid = []
    row_index = 0
    for row in number_grid:
        object_row = []
        column_index = 0
        for number in row:
            if number == '0':  # ścieżka
                object_row.append(Cell(float('inf'), True, [column_index, row_index]))
            elif number == '1':  # ściana
                object_row.append(Cell(float('inf'), False, [column_index, row_index]))
            elif number == '2':  # drzwi
                object_row.append(Cell(float('inf'), False, [column_index, row_index], 'nn'))
            else:
                object_row.append(Cell(float('inf'), False, [column_index, row_index], number))
            column_index += 1
        object_grid.append(object_row)
        row_index += 1
    return object_grid


# def test():
#     board = read_board()
#     obj_board = number_to_object_grid(board)
#     for row in obj_board:
#         print(row)

# test()
