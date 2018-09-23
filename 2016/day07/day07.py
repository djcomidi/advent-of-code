import re


def contains_abba(s):
    for i in range(0, len(s) - 3):
        if s[i] != s[i+1] and s[i:i+4] == s[i:i+4][::-1]:
            return True
    return False


def supports_tls(address):
    parts = re.split("\[|\]", address)
    hypernet = False
    support = False
    for part in parts:
        if hypernet:
            if contains_abba(part):
                return False
        else:
            if contains_abba(part):
                support = True
        hypernet = not hypernet
    return support


def find_needles(s):
    for i in range(0, len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            yield s[i:i+3]


def supports_ssl(address):
    parts = re.split("\[|\]", address)
    hypernet = False
    needlesA, needlesB = set([]), set([])
    for part in parts:
        if hypernet:
            for needle in find_needles(part):
                newndl = needle[1] + needle[0] + needle[1]
                needlesB.add(newndl)
        else:
            for needle in find_needles(part):
                needlesA.add(needle)
        hypernet = not hypernet
    return len(needlesA & needlesB) > 0


with open('day07.txt') as f:
    data = f.read()

addresses = data.strip().split('\n')

if False:
    addresses = [
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn'
    ]

supported = 0
for address in addresses:
    if supports_tls(address):
        supported += 1
print("Day 07: Answer Part 1:", supported)

if False:
    addresses = [
        'aba[bab]xyz',
        'xyx[xyx]xyx',
        'aaa[kek]eke',
        'zazbz[bzb]cdb'
    ]

supported = 0
for address in addresses:
    if supports_ssl(address):
        supported += 1
print("Day 07: Answer Part 2:", supported)
