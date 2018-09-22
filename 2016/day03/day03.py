with open('day03.txt') as f:
    lines = f.read().strip().split('\n')

triangles = [list(map(int, line.split())) for line in lines]

possibles = 0
for triangle in triangles:
    largest = max(triangle)
    if sum(triangle) - largest > largest:
        possibles += 1

print("Day 03: Answer Part 1:", possibles)

possibles = 0
for r in range(0, len(triangles), 3):
    for c in range(0, len(triangles[r])):
        triangle = [triangles[r][c], triangles[r+1][c], triangles[r+2][c]]
        largest = max(triangle)
        if sum(triangle) - largest > largest:
            possibles += 1

print("Day 03: Answer Part 2:", possibles)
