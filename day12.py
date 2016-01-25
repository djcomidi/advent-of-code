import json


def sumnums(x, excl_red):
    if isinstance(x, dict):
        if excl_red and "red" in x.values():
            return 0
        return sum(sumnums(v, excl_red) for v in x.values())
    if isinstance(x, int):
        return x
    if isinstance(x, str):
        return 0
    if isinstance(x, list):
        return sum(sumnums(t, excl_red) for t in x)
    return 0

with open('day12.txt') as f:
    data = f.read()
jsondata = json.loads(data)

print("Day 12: Answer Part 1:", sumnums(jsondata, False))
print("Day 12: Answer Part 2:", sumnums(jsondata, True))
