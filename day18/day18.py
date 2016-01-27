from pprint import pprint

SIZE = 100


def data_to_grid(data):
    grid = dict()
    for y, line in enumerate(data):
        for x, c in enumerate(line.strip()):
            grid[(x, y)] = c == "#"
    return grid


def count_neighbors(grid, x, y):
    neighbors = -1 if grid[(x, y)] else 0
    for yt in [-1, 0, 1]:
        for xt in [-1, 0, 1]:
            neighbors += 1 if grid.get((x+xt, y+yt), False) else 0
    return neighbors


def mark_corners_on(grid):
    for (x, y) in [(0, 0), (0, SIZE-1), (SIZE-1, 0), (SIZE-1, SIZE-1)]:
        grid[(x, y)] = True
    return grid


def next_generation(grid, corner_rule=False):
    newgrid = dict()
    for y in range(SIZE):
        for x in range(SIZE):
            neighbors = count_neighbors(grid, x, y)
            if grid[(x, y)]:
                newgrid[(x, y)] = neighbors in [2, 3]
            else:
                newgrid[(x, y)] = neighbors == 3
    if corner_rule:
        newgrid = mark_corners_on(newgrid)
    return newgrid

with open('day18.txt') as f:
    lines = f.readlines()

grid = data_to_grid(lines)
for i in range(100):
    grid = next_generation(grid)
n_lights_on = list(grid.values()).count(True)
print("Day 18: Answer Part 1:", n_lights_on)

grid = data_to_grid(lines)
grid = mark_corners_on(grid)
for i in range(100):
    grid = next_generation(grid, corner_rule=True)
n_lights_on = list(grid.values()).count(True)
print("Day 18: Answer Part 2:", n_lights_on)
