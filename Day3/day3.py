def tree_count_by_slope(grid: list, slope_x: int, slope_y: int):
    rows = len(grid)
    cols = len(grid[0])

    tree_count = 0
    open_count = 0

    current_x = 0
    current_y = 0

    path_map = {}

    while current_y < rows - 1:
        current_x = (current_x + slope_x) % cols
        current_y = current_y + slope_y
        path_map[(current_x, current_y)] = grid[current_y][current_x]

    values = list(path_map.values())
    tree_count = values.count("#")
    open_count = values.count(".")

    return tree_count


def result(slopes: list, func) -> int:
    with open("./Day3/input.txt", "rt") as f:
        grid = [line.strip() for line in f.readlines()]

    multiplied_result = 1

    for slope in slopes:
        slope_x = slope[0]
        slope_y = slope[1]

        multiplied_result = multiplied_result * func(grid, slope_x, slope_y)

    return multiplied_result


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

r = result(slopes, tree_count_by_slope)