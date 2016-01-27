from pprint import pprint

with open('day21.txt') as f:
    bH = int(f.readline().strip().split()[-1])
    bD = int(f.readline().strip().split()[-1])
    bA = int(f.readline().strip().split()[-1])

WEAPONS, ARMOR, RINGS = [], [], []
with open('day21_items.txt') as f:
    for line in f.readlines():
        cat, n, c, d, a = line.strip().split(",")
        item = (n, int(c), int(d), int(a))
        if cat == 'w':
            WEAPONS.append(item)
        elif cat == 'a':
            ARMOR.append(item)
        elif cat == 'r':
            RINGS.append(item)

N, C, D, A = 0, 1, 2, 3
A_CHOICES = [[], [0], [1], [2], [3], [4]]
R_CHOICES = [[], [0], [1], [1, 0], [2], [2, 0], [2, 1],
             [3], [3, 0], [3, 1], [3, 2],
             [4], [4, 0], [4, 1], [4, 2], [4, 3],
             [5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]

cda = set()
least_win_cost, most_loss_cost = 10**10, -1
for weapon in WEAPONS:
    for aa in A_CHOICES:
        for rr in R_CHOICES:
            mC, mD, mA = weapon[C], weapon[D], weapon[A]
            for armor in [ARMOR[x] for x in aa]:
                mC, my, mA = mC + armor[C], mD + armor[D], mA + armor[A]
            for ring in [RINGS[x] for x in rr]:
                mC, mD, mA = mC + ring[C], mD + ring[D], mA + ring[A]
            cda.add((mC, mD, mA))
            if (bD-mA) <= (mD-bA):
                least_win_cost = min(least_win_cost, mC)
            else:
                most_loss_cost = max(most_loss_cost, mC)
print("Day 21: Answer Part 1:", least_win_cost)
print("Day 21: Answer Part 2:", most_loss_cost)
