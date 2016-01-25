from itertools import permutations

with open('day09.txt') as f:
    lines = [line.strip() for line in f.readlines()]

distances = {}
cities = set([])
for line in lines:
    cityA, _, cityB, _, dist = line.split(' ')
    cities.add(cityA)
    cities.add(cityB)
    distances[(cityA, cityB)] = int(dist, 10)
    distances[(cityB, cityA)] = int(dist, 10)

shortest, longest = sum(distances.values()), 0
steps = len(cities) - 1
for path in permutations(cities):
    pathlen = sum(distances[(path[i], path[i+1])] for i in range(0, steps))
    shortest = min(shortest, pathlen)
    longest = max(longest, pathlen)
print("Day 09: Answer Part 1:", shortest)
print("Day 09: Answer Part 2:", longest)
