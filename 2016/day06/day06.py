from collections import Counter


with open('day06.txt') as f:
    data = f.read()

lines = data.strip().split('\n')
columns = [""] * len(lines[0])
for line in lines:
    for i, c in enumerate(line):
        columns[i] += c

message = ""
for column in columns:
    counter = Counter(column)
    most = counter.most_common(1)[0][0]
    message += most
print("Day 06: Answer Part 1:", message)

message = ""
for column in columns:
    counter = Counter(column)
    least = counter.most_common()[-1][0]
    message += least
print("Day 06: Answer Part 2:", message)
