def count_combos(store, avails, combo=[]):
    if store == 0:
        return 1
    n = 0
    low = 0 if len(combo) == 0 else combo[-1] + 1
    for i in range(low, len(avails)):
        n += count_combos(store-avails[i], avails, combo+[i])
    return n


def count_min_combos(store, avails, combo=[]):
    if store == 0:
        return (len(combo), 1)
    lowest = (len(avails), 1)
    low = 0 if len(combo) == 0 else combo[-1] + 1
    for i in range(low, len(avails)):
        cmb = count_min_combos(store-avails[i], avails, combo+[i])
        if cmb[0] == lowest[0]:
            lowest = (lowest[0], lowest[1]+cmb[1])
        elif cmb[0] < lowest[0]:
            lowest = cmb
    return lowest


with open('day17.txt') as f:
    containers = [int(line.strip()) for line in f.readlines()]
    containers = sorted(containers)

combos = count_combos(150, containers)
print("Day 17: Answer Part 1:", combos)

min_combos = count_min_combos(150, containers)
print("Day 17: Answer Part 2:", min_combos[1])
