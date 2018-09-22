KEYPAD_ONE = ["123", "456", "789"]
KEYPAD_TWO = ["..1..", ".234.", "56789", ".ABC.", "..D.."]

with open('day02.txt') as f:
    data = f.readlines()
lines = [line.strip() for line in data]

# lines = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

x, y = 1, 1
secret = ""
for line in lines:
    for dir in line:
        if dir == "U":
            y = max(0, y - 1)
        elif dir == "L":
            x = max(0, x - 1)
        elif dir == "D":
            y = min(len(KEYPAD_ONE) - 1, y + 1)
        elif dir == "R":
            x = min(len(KEYPAD_ONE[0]) - 1, x + 1)
    secret += KEYPAD_ONE[y][x]

print("Day 02: Answer Part 1:", secret)


x, y = 0, 2
secret = ""
for line in lines:
    for dir in line:
        newx, newy = x, y
        if dir == "U":
            newy = max(0, newy - 1)
        elif dir == "L":
            newx = max(0, newx - 1)
        elif dir == "D":
            newy = min(len(KEYPAD_TWO) - 1, newy + 1)
        elif dir == "R":
            newx = min(len(KEYPAD_TWO[0]) - 1, newx + 1)
        if KEYPAD_TWO[newy][newx] != ".":
            x, y = newx, newy
    secret += KEYPAD_TWO[y][x]

print("Day 02: Answer Part 2:", secret)
