MAGIC_MISSILE, DRAIN, SHIELD, POISON, RECHARGE = 0, 1, 2, 3, 4

BOSS, PLAYER = 1, 2
COSTS = [53, 73, 113, 173, 229]
TIMERS = [1, 1, 6, 6, 5]
NAMES = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
INF = 10**8
g_low, g_hard = INF, False


def apply_spell(stats, sid, timer):
    if timer == TIMERS[sid] - 1:
        stats["pM"] -= COSTS[sid]
    if sid == MAGIC_MISSILE:
        stats["bH"] -= 4
    elif sid == DRAIN:
        stats["pH"] += 2
        stats["bH"] -= 2
    elif sid == SHIELD:
        if timer == TIMERS[SHIELD] - 1:
            stats["pA"] += 7
        elif timer == 0:
            stats["pA"] -= 7
    elif sid == POISON:
        stats["bH"] -= 3
    elif sid == RECHARGE:
        stats["pM"] += 101
    return stats


def apply_spells(stats, spells):
    newspells = []
    for sid, timer in spells:
        timer -= 1
        stats = apply_spell(stats, sid, timer)
        if timer > 0:
            newspells += [(sid, timer)]
    return stats, newspells


def play_game(stats, spells=[], player=PLAYER, cost=0):
    global g_low
    if stats["pH"] <= 0 or stats["pM"] < min(COSTS) or cost > g_low:
        return INF
    newstats, newspells = apply_spells(stats.copy(), spells)
    if newstats["bH"] <= 0:
        return cost
    if player == BOSS:
        newstats["pH"] = newstats["pH"] - newstats["bD"] + newstats["pA"]
        return play_game(newstats, newspells, PLAYER, cost)
    if g_hard:
        newstats["pH"] -= 1
        if newstats["pH"] <= 0:
            return INF
    lowcost = INF
    avails = set([0, 1, 2, 3, 4]) - set(s[0] for s in newspells)
    for sid in [i for i in avails if COSTS[i] < stats["pM"]]:
        newspells += [(sid, TIMERS[sid])]
        newcost = cost + COSTS[sid]
        lowcost = min(lowcost, play_game(newstats, newspells, BOSS, newcost))
        newspells = newspells[:-1]
    g_low = min(g_low, lowcost)
    return lowcost


def find_min_game(stats, hard=False):
    global g_low, g_hard
    g_low, g_hard = INF, hard
    return play_game(stats)

with open('day22.txt') as f:
    bH = int(f.readline().strip().split()[-1])
    bD = int(f.readline().strip().split()[-1])
    stats = {"pH": 50, "pA": 0, "pM": 500, "bH": bH, "bD": bD}

print("Day 22: Answer Part 1:", find_min_game(stats))
print("Day 22: Answer Part 2:", find_min_game(stats, hard=True))
