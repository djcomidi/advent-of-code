with open('day06.txt') as f:
    lines = f.readlines()

LIMIT = 1000 * 1000
state = [False] * LIMIT
brightness = [0] * LIMIT
for line in lines:
    parts = line.split(' ')
    x0, y0 = [int(p) for p in parts[-3].split(',')]
    x1, y1 = [int(p) for p in parts[-1].split(',')]
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            id = 1000 * y + x
            if line[:6] == 'toggle':
                state[id] = not state[id]
                brightness[id] += 2
            elif line[:8] == 'turn off':
                state[id] = False
                brightness[id] = max(0, brightness[id] - 1)
            elif line[:7] == 'turn on':
                state[id] = True
                brightness[id] += 1
print("Day 06: Answer Part 1:", state.count(True))
print("Day 06: Answer Part 2:", sum(brightness))
