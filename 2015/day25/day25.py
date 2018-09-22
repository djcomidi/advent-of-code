with open('day25.txt') as f:
    parts = f.readline().strip().split(" ")
    ROW = int(parts[-3][:-1])
    COL = int(parts[-1][:-1])

r, c, val = 1, 1, 20151125
while not (r == ROW and c == COL):
    if r == 1:
        r, c = c + 1, 1
    else:
        r, c = r - 1, c + 1
    val = (val * 252533) % 33554393
print("Day 25: Answer Part 1:", val)
