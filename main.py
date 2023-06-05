from dijkstra import find_path_dijkstra
from opening_a_file import read_board, number_to_object_grid


def find_x(obj_board) -> list:
    x_coordinates = []
    for column in obj_board:
        for element in column:
            if element.weight == -1:
                x_coordinates.append(element.coordinates)
    return x_coordinates


def show_result(obj_board: list, path: list):
    row_index = 0
    result = ""
    for row in obj_board:
        column_index = 0
        for cell in row:
            if cell not in path:
                result += " "
            elif cell.weight == -1:
                result += "X"
            else:
                result += str(cell.weight)
            column_index += 1
        row_index += 1
        result += '\n'

    print(result)


def main():
    board = read_board()
    obj_board = number_to_object_grid(board)
    start_and_end_coords = find_x(obj_board)
    path = find_path_dijkstra(start_and_end_coords[0], start_and_end_coords[1], obj_board)
    show_result(obj_board, path)


if __name__ == "__main__":
    main()
