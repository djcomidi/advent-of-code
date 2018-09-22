import re
from itertools import groupby
from string import ascii_lowercase as lowercases

testrooms = [
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]'
]


def parse_room(room):
    m = re.search(r'(.*)-(\d+)\[([a-z]+)\]', room)
    name, sector, check = m.group(1), int(m.group(2)), m.group(3)
    name = re.sub('[-]', '', name)
    occurs = [(len(list(g)), k) for k, g in groupby(sorted(name))]
    occurs.sort(key=lambda x: -x[0] - 1.0/ord(x[1]))
    realcheck = "".join(x[1] for x in occurs[:5])
    if realcheck == check:
        return {'name': name, 'sector': sector, 'check': check}
    else:
        return None


def decrypt(name, sector):
    shift = sector % 26
    plain = ""
    for c in name:
        if c in lowercases:
            plain += chr(ord('a') + (ord(c) - ord('a') + shift) % 26)
        elif c == '-':
            plain += ' '
    return plain


with open('day04.txt') as f:
    rooms = f.read().strip().split('\n')

# rooms = testrooms[:]

sectorsum = 0
for room in rooms:
    data = parse_room(room)
    if data:
        sectorsum += data['sector']

print("Day 04: Answer Part 1:", sectorsum)

npsector = None
for room in rooms:
    data = parse_room(room)
    if data:
        name = decrypt(data['name'], data['sector'])
        if name[:9] == 'northpole':
            npsector = data['sector']

print("Day 04: Answer Part 2:", npsector)
