from itertools import permutations


def calc_max_happiness(guests, happiness):
    NGUESTS = len(guests)
    maxhappy = 0
    for seats in permutations(guests):
        happy = 0
        for i in range(NGUESTS):
            left = seats[(i-1+NGUESTS) % NGUESTS]
            right = seats[(i+1) % NGUESTS]
            g = seats[i]
            happy += happiness[(g, left)]
            happy += happiness[(g, right)]
        maxhappy = max(maxhappy, happy)
    return maxhappy

with open('day13.txt') as f:
    lines = [line.strip() for line in f.readlines()]
guests = set()
happiness = dict()
for line in lines:
    guestA, _, delta, amount, _, _, _, _, _, _, guestB = line[:-1].split(" ")
    guests.add(guestA)
    guests.add(guestB)
    points = int(amount) if delta == "gain" else -int(amount)
    happiness[(guestA, guestB)] = points

maxhappy = calc_max_happiness(guests, happiness)
print("Day 13: Answer Part 1:", maxhappy)

ME = "Myself"
for g in guests:
    happiness[(g, ME)] = 0
    happiness[(ME, g)] = 0
guests.add(ME)
mehappy = calc_max_happiness(guests, happiness)
print("Day 13: Answer Part 2:", mehappy)
