def spoongen(ningr=4, nspoons=100, spoons=[]):
    if ningr == 1:
        yield spoons+[nspoons]
    else:
        for t in range(1, nspoons+1):
            for sp in spoongen(ningr-1, nspoons-t, spoons+[t]):
                yield sp

names, capacity, durability, flavor, texture, calories = [], [], [], [], [], []
with open('day15.txt') as f:
    for line in f.readlines():
        parts = line.strip().split(' ')
        names += [parts[0][:-1]]
        capacity += [int(parts[2][:-1])]
        durability += [int(parts[4][:-1])]
        flavor += [int(parts[6][:-1])]
        texture += [int(parts[8][:-1])]
        calories += [int(parts[10])]

ningr = len(names)
max_score_spoons, max_score_cals = 0, 0
for spoons in spoongen(ningr=ningr, nspoons=100):
    cap = max(0, sum(capacity[i]*spoons[i] for i in range(ningr)))
    dur = max(0, sum(durability[i]*spoons[i] for i in range(ningr)))
    flv = max(0, sum(flavor[i]*spoons[i] for i in range(ningr)))
    tex = max(0, sum(texture[i]*spoons[i] for i in range(ningr)))
    cal = max(0, sum(calories[i]*spoons[i] for i in range(ningr)))
    score = cap * dur * flv * tex
    max_score_spoons = max(max_score_spoons, score)
    if cal == 500:
        max_score_cals = max(max_score_cals, score)
print("Day 15: Answer Part 1:", max_score_spoons)
print("Day 15: Answer Part 2:", max_score_cals)
