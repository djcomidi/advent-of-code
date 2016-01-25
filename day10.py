from itertools import groupby


def look_and_say(t):
    return ''.join("%d%s" % (len(list(g)), k) for k, g in groupby(t))

t = "1321131112"
solA, solB = 0, 0
for i in range(50):
    t = look_and_say(t)
    if i == 39:
        solA = len(t)
    if i == 49:
        solB = len(t)
#    print(i, len(t))
print("Day 10: Answer Part 1:", solA)
print("Day 10: Answer Part 2:", solB)
