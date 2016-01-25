def is_nice_a(w):
    # It does not contain the strings ab, cd, pq, or xy
    if any(sub in w for sub in ['ab', 'cd', 'pq', 'xy']):
        return False
    # It contains at least three vowels (aeiou only)
    if sum(w.count(vowel) for vowel in 'aeiou') < 3:
        return False
    # It contains at least one letter that appears twice in a row
    doubles = 0
    for i in range(len(w)-1):
        doubles += 1 if w[i] == w[i+1] else 0
    return doubles > 0


def is_nice_b(w):
    # a pair of two letters that appears at least twice without overlapping
    # at least one letter which repeats with exactly one letter between them
    pairs, singles = 0, 0
    for i in range(len(w)-2):
        pairs += 1 if w[i:i+2] in w[i+2:] else 0
        singles += 1 if w[i] == w[i+2] else 0
    return pairs > 0 and singles > 0

with open('day05.txt') as f:
    words = f.readlines()

nicesA, nicesB = 0, 0
for word in words:
    nicesA += 1 if is_nice_a(word) else 0
    nicesB += 1 if is_nice_b(word) else 0
print("Day 05: Answer Part 1:", nicesA)
print("Day 05: Answer Part 2:", nicesB)
