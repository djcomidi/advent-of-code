KNOWN = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
    'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1
}

aunts = []
with open('day16.txt') as f:
    for line in f.readlines():
        p = line.strip().split(" ")
        aunt = dict()
        aunt[p[2][:-1]] = int(p[3][:-1])
        aunt[p[4][:-1]] = int(p[5][:-1])
        aunt[p[6][:-1]] = int(p[7])
        aunts.append(aunt)

giftaunt = 0
for n, aunt in enumerate(aunts):
    same = True
    for k, v in aunt.items():
        same = same and KNOWN[k] == v
    if same:
        giftaunt = n + 1
print("Day 16: Answer Part 1:", giftaunt)

realaunt = 0
for n, aunt in enumerate(aunts):
    same = True
    for k, v in aunt.items():
        if k in ["cats", "trees"]:
            same = same and KNOWN[k] < v
        elif k in ["pomeranians", "goldfish"]:
            same = same and KNOWN[k] > v
        else:
            same = same and KNOWN[k] == v
    if same:
        realaunt = n + 1
print("Day 16: Answer Part 2:", realaunt)
