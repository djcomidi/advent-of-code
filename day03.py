with open('day03.txt') as f:
    data = f.read()

houses = {(0, 0)}
px, py = 0, 0
for dir in data:
    if dir == '^':
        py -= 1
    elif dir == 'v':
        py += 1
    elif dir == '<':
        px -= 1
    elif dir == '>':
        px += 1
    houses.add((px, py))
print("Day 03: Answer Part 1:", len(houses))

santas, robos = {(0, 0)}, {(0, 0)}
sx, sy, rx, ry = 0, 0, 0, 0
for i, dir in enumerate(data):
    if i % 2 == 0:
        if dir == '^':
            sy -= 1
        elif dir == 'v':
            sy += 1
        elif dir == '<':
            sx -= 1
        elif dir == '>':
            sx += 1
        santas.add((sx, sy))
    else:
        if dir == '^':
            ry -= 1
        elif dir == 'v':
            ry += 1
        elif dir == '<':
            rx -= 1
        elif dir == '>':
            rx += 1
        robos.add((rx, ry))
print("Day 03: Answer Part 2:", len(santas | robos))
