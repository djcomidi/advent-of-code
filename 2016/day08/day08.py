import re

WIDTH, HEIGHT = 50, 6

with open('day08.txt') as f:
    lines = f.readlines()

instructions = [line.strip() for line in lines]

lights = set([])
for instruction in instructions:
    nums = re.findall(r'\d+', instruction)
    if instruction[:4] == 'rect':
        width, height = int(nums[0]), int(nums[1])
        lights |= set((x, y) for x in range(width) for y in range(height))
    elif instruction[:10] == 'rotate row':
        row, shift = int(nums[0]), int(nums[1])
        oldcells = set(cell for cell in lights if cell[1] == row)
        newcells = set(((c[0] + shift) % WIDTH, c[1]) for c in oldcells)
        lights -= oldcells
        lights |= newcells
    elif instruction[:10] == 'rotate col':
        col, shift = int(nums[0]), int(nums[1])
        oldcells = set(cell for cell in lights if cell[0] == col)
        newcells = set((c[0], (c[1] + shift) % HEIGHT) for c in oldcells)
        lights -= oldcells
        lights |= newcells


print("Day 08: Answer Part 1:", len(lights))


print("Day 08: Answer Part 2:")
for y in range(HEIGHT):
    for x in range(WIDTH):
        if (x, y) in lights:
            print("#", end="")
        else:
            print(" ", end="")
    print()
