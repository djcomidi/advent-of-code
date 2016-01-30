from itertools import product, permutations, filterfalse
from functools import reduce
from operator import mul

# SOLUTION PART 1 = len:6 qe:10723906903
INF = 10**10


def groupgen(weights, target, sub=[]):
    if sum(sub) == target:
        yield []
    else:
        for i, w in enumerate([t for t in weights if t <= target - sum(sub)]):
            for g in groupgen(weights[i+1:], target, sub+[w]):
                yield [w] + g


def get_first(weights, target):
    x = None
    for g in groupgen(weights, target):
        x = g
        break
    return x

with open('day24.txt') as f:
    weights = [int(w.strip()) for w in f.readlines()]

target = sum(weights) // 3
lown, lowqe = INF, INF
for G1 in groupgen(weights, target):
    if len(G1) > lown:
        continue
    others = sorted(set(weights) - set(G1))
    if get_first(others, target) is None:
        continue
    qe = reduce(mul, G1, 1)
    if len(G1) == lown:
        lowqe = min(lowqe, qe)
    elif len(G1) < lown:
        lown, lowqe = len(G1), qe
print("Day 24: Answer Part 1:", lowqe)

target = sum(weights) // 4
lown, lowqe = INF, INF
for G1 in groupgen(weights, target):
    if len(G1) > lown:
        continue
    othersA = sorted(set(weights) - set(G1))
    G2 = get_first(othersA, target)
    if G2 is None:
        continue
    othersB = sorted(set(weights) - set(G1) - set(G2))
    if get_first(othersB, target) is None:
        continue
    qe = reduce(mul, G1, 1)
    if len(G1) == lown:
        lowqe = min(lowqe, qe)
    elif len(G1) < lown:
        lown, lowqe = len(G1), qe
print("Day 24: Answer Part 2:", lowqe)
