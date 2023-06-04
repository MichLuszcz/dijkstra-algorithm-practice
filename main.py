from dijkstra import find_path_dijkstra
from opening_a_file import read_board, number_to_object_grid


def show_result(obj_board: list, path: list):
    row_index = 0
    for row in obj_board:
        column_index = 0
        for cell in row:
            if cell not in path:
                obj_board[row_index][column_index] = " "
            else:
                obj_board[row_index][column_index] = str(cell.weight)
            column_index += 1
        row_index += 1

    result = ""
    for row in obj_board:
        for element in row:
            if element.isnumeric():
                result += element
            else:
                result += " "
        result += '\n'

    print(result)


def main():
    board = read_board()
    obj_board = number_to_object_grid(board)
    path = find_path_dijkstra([1, 1], [2, 4], obj_board)
    show_result(obj_board, path)


if __name__ == "__main__":
    main()
