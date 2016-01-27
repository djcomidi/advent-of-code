DBLQUOTE, BACKSLASH, KEY_X = 34, 92, 120


def size_in_mem(w):
    w, i, cnt = w[1:-1], 0, 0
    while i < len(w):
        if w[i] == BACKSLASH and w[i+1] in [BACKSLASH, DBLQUOTE]:
            i, cnt = i+2, cnt+1
        elif w[i] == BACKSLASH and w[i+1] == KEY_X:
            i, cnt = i+4, cnt+1
        else:
            i, cnt = i+1, cnt+1
    return cnt


def size_in_encoding(w):
    t, i = 2, 0
    for b in w:
        t += 1
        if b in [BACKSLASH, DBLQUOTE]:
            t += 1
    return t

words = []
with open('day08.txt', 'rb') as f:
    words = f.readlines()
    words = [w[:-1] for w in words]

# words = [rb'""', rb'"abc"', rb'"aaa\"aaa"', rb'"\x27"']
diffA, diffB = 0, 0
for w in words:
    sic, sim, sie = len(w), size_in_mem(w), size_in_encoding(w)
#    print("%2d %2d %2d %s" % (sic, sim, sie, w))
    diffA += sic - sim
    diffB += sie - sic
print("Day 08: Answer Part 1:", diffA)
print("Day 08: Answer Part 2:", diffB)
