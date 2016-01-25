import re

LENGTH = 8
LETTERS = "abcdefghijklmnopqrstuvwxyz"
LIMIT = len(LETTERS)**LENGTH


def rotate(w):
    wid = sum((ord(w[i]) - 97) * 26**(7-i) for i in range(LENGTH))
    newt, q = "", (wid + 1) % LIMIT
    for i in range(LENGTH):
        q, r = divmod(q, 26)
        newt = chr(ord('a') + r) + newt
    return newt


def is_valid(t):
    # Passwords may not contain the letters i, o, or l
    if any(c in t for c in "iol"):
        return False
    # Passwords must include one increasing straight of at least three letters
    if not any(LETTERS[i:i+3] in t for i in range(24)):
        return False
    # Passwords must contain at least two different, non-overlapping pairs
    pairs = [m.group() for m in re.finditer(r'((\w)\2)', t)]
    if len(set(pairs)) < 2:
        return False
    return True


def next_valid(w):
    w = rotate(w)
    while not is_valid(w):
        w = rotate(w)
    return w

pwdA = next_valid("cqjxjnds")
pwdB = next_valid(pwdA)
print("Day 11: Answer Part 1:", pwdA)
print("Day 11: Answer Part 2:", pwdB)
