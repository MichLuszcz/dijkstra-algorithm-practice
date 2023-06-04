from CellClass import Cell


def get_closest_cell(cell_list: list):
    if not cell_list:
        return
    current = cell_list[0]
    closest = cell_list[0]
    for cell in cell_list:
        if (current.distance < closest.distance):
            closest = current
    return closest


Coordinates = list
Grid = [[Cell]]


def find_path_dijkstra(start: Coordinates,
                       goal: Coordinates,
                       grid: Grid,) -> list:
    path = []  # Cells
    grid_height = len(grid)
    grid_width = len(grid[0])
    start[0] = abs(start[0])
    start[1] = abs(start[1])  # probably not neccessary?
    start_cell = grid[start[1]][start[0]]
    goal_cell = grid[goal[1]][goal[0]]
    if (start == goal):
        return [start_cell]

    start_cell.distance = 0
    unexplored_cells = all_values(grid)  # array of Cells

    while (goal_cell in unexplored_cells):
        closest = get_closest_cell(unexplored_cells)
        [x, y] = closest.coordinates
        neighbours = []
        if (y != 0):
            neighbours.append(grid[y-1][x])
        if (x != 0):
            neighbours.append(grid[y][x-1])
        if (y != grid_height):
            neighbours.append(grid[y+1][x])
        if (x != grid_width):
            neighbours.append(grid[y][x+1])
        for neighbour in neighbours:
            # iterating over every neighbour
            # and updating their distances if needed
            if (neighbour.is_walkable or neighbour == goal_cell):
                # sprawdza czy da się przejść lub czy jest u celu
                if (neighbour.distance > closest.distance + neighbour.weight):
                    neighbour.distance = closest.distance + neighbour.weight
                    # and setting the current cell as their parent
                    neighbour.parent_coordinates = closest.coordinates
        unexplored_cells.remove(closest)  # mark the cell as explored

    current_cell = goal_cell
    while (current_cell != start_cell):
        #   making the array of all parents of the final cell
        path.append(current_cell)
        next_coordinates = current_cell.parent_coordinates
        if (next_coordinates is None):
            return []

        current_cell = grid[next_coordinates[1]][next_coordinates[0]]

    path.append(current_cell)  # adding the starting cell to the end
    path.reverse()      # changing the path from finish-start to start-finish
    return path


def all_values(array_2d):
    values = []
    for row in array_2d:
        values += str(row)
    return values
