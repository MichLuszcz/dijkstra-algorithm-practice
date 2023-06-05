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
            elif element == "-1":
                result += "X"
            else:
                result += " "
        result += '\n'

    print(result)


def find_start_and_finish(grid: list(list())):
    findings = []
    for row in grid:
        for cell in row:
            if cell.weight == -1:
                findings.append(cell.coordinates)
    return findings


def main():
    board = read_board()
    obj_board = number_to_object_grid(board)
    start_finish = find_start_and_finish(obj_board)
    path = find_path_dijkstra(start_finish[0], start_finish[1], obj_board)
    show_result(obj_board, path)
    print(board)


if __name__ == "__main__":
    main()
