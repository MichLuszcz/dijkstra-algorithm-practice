from dijkstra import find_path_dijkstra
from opening_a_file import read_board, number_to_object_grid


def main():
    board = read_board()
    obj_board = number_to_object_grid(board)
    path = find_path_dijkstra([1, 1], [2, 4], obj_board)
    print(path)


if __name__ == "__main__":
    main()
