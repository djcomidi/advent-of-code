COMPASS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open('day01.txt') as f:
    data = f.read().strip()

# data = "R2, L3"
# data = "R2, R2, R2"
# data = "R5, L5, R5, R3"

instructions = data.split(", ")

x, y = 0, 0
dir = 0
for instruction in instructions:
    turn, steps = instruction[0], int(instruction[1:])
    d = 1 if turn == 'R' else -1
    dir = (dir + d) % len(COMPASS)
    dx, dy = COMPASS[dir]
    x, y = x + dx * steps, y + dy * steps

distance = abs(x) + abs(y)
print("Day 01: Answer Part 1:", distance)


visited = set()
x, y = 0, 0
dir = 0
first_double = None
for instruction in instructions:
    turn, steps = instruction[0], int(instruction[1:])
    d = 1 if turn == 'R' else -1
    dir = (dir + d) % len(COMPASS)
    dx, dy = COMPASS[dir]
    for i in range(steps):
        xi, yi = x + dx * i, y + dy * i
        if (xi, yi) in visited:
            first_double = (xi, yi)
            break
        else:
            visited.add((xi, yi))
    x, y = x + dx * steps, y + dy * steps
    if first_double:
        break

distance = abs(first_double[0]) + abs(first_double[1])
print("Day 01: Answer Part 2:", distance)
