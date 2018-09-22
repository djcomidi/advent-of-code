def advance(x, y, to):
    if to == '^':
        return x, y-1
    elif to == 'v':
        return x, y+1
    elif to == '<':
        return x-1, y
    elif to == '>':
        return x+1, y
    return 0, 0

with open('day03.txt') as f:
    data = f.read()

houses = {(0, 0)}
px, py = 0, 0
for dir in data:
    px, py = advance(px, py, dir)
    houses.add((px, py))
print("Day 03: Answer Part 1:", len(houses))

santas, robos = {(0, 0)}, {(0, 0)}
sx, sy, rx, ry = 0, 0, 0, 0
for i, dir in enumerate(data):
    if i % 2 == 0:
        sx, sy = advance(sx, sy, dir)
        santas.add((sx, sy))
    else:
        rx, ry = advance(rx, ry, dir)
        robos.add((rx, ry))
print("Day 03: Answer Part 2:", len(santas | robos))
