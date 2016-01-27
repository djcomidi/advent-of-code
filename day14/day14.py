def get_distance(runner, t):
    speed, flytime, resttime = runner[1], runner[2], runner[3]
    interval = flytime + resttime
    completed, remain = divmod(t, interval)
    dist = completed * speed * flytime
    dist += min(flytime, remain) * speed
    return dist

with open('day14.txt') as f:
    lines = [line.strip() for line in f.readlines()]
runners = []
for line in lines:
    p = line.split(" ")
    name, speed, flytime, resttime = p[0], int(p[3]), int(p[6]), int(p[13])
    runners.append((name, speed, flytime, resttime))

MAXTIME = 2503
maxdist = 0
for runner in runners:
    dist = get_distance(runner, MAXTIME)
    maxdist = max(maxdist, dist)
print("Day 14: Answer Part 1:", maxdist)

scores = [0] * len(runners)
for t in range(1, MAXTIME+1):
    dists = [get_distance(r, t) for r in runners]
    maxdist = max(dists)
    for i, d in enumerate(dists):
        if d == maxdist:
            scores[i] += 1
print("Day 14: Answer Part 1:", max(scores))
