from hashlib import md5
from pprint import pprint


def find_next_a(door, suffix):
    solution = None
    while not solution:
        suffix += 1
        key = f"{door}{suffix}"
        hash = md5(key.encode()).hexdigest()
        if hash[:5] == '00000':
            solution = (hash, suffix)
    return solution


def find_next_b(door, suffix, visited):
    solution = None
    while not solution:
        suffix += 1
        key = f"{door}{suffix}"
        hash = md5(key.encode()).hexdigest()
        if hash[:5] != '00000':
            continue
        if hash[5] not in visited and '0' <= hash[5] <= '7':
            solution = (hash, suffix, visited + hash[5])
    return solution


door = "cxdnnyjw"
# door = "abc"

suffix = 1
key = ""
for i in range(8):
    hash, suffix = find_next_a(door, suffix)
    key += hash[5]

print("Day 05: Answer Part 1:", key)

suffix = 1
key = list("________")
visited = ""
for i in range(8):
    hash, suffix, visited = find_next_b(door, suffix, visited)
    idx = int(hash[5])
    key[idx] = hash[6]
print("Day 05: Answer Part 2:", "".join(key))
