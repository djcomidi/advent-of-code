with open('day01.txt') as f:
    data = f.read()

level = data.count('(') - data.count(')')
print("Day 01: Answer Part 1:", level)

level, pos = 0, 0
for c in data:
    pos += 1
    if c == '(':
        level += 1
    elif c == ')':
        level -= 1
    if level == -1:
        break
print("Day 01: Answer Part 2:", pos)
