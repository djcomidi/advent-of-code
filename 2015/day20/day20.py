from gmpy2 import next_prime
from functools import reduce
from operator import mul

INPUT = 33100000


def calc_presents(primes):
    sod = 1
    for p in set(primes):
        sod *= (p**(primes.count(p)+1)-1)//(p-1)
    return sod


def find_min_house(primes=[]):
    house, presents = reduce(mul, primes, 1), calc_presents(primes)
    # 2**22-1 > TARGET, so there can be no more #primes than 21
    if len(primes) > 21:
        return 10**8
    if 10*presents >= INPUT:
        return house
    p = 2 if len(primes) == 0 else primes[-1]
    lowh = 10**8
    # after examination, this seemed like a fair upperbound
    while p < 24:
        lowh = min(lowh, find_min_house(primes + [int(p)]))
        p = next_prime(p)
    return lowh
print("Day 20: Answer Part 1:", find_min_house())

presents, elf, lowh = dict(), 1, -1
while lowh == -1:
    for i in range(1, 51):
        presents[elf*i] = presents.get(elf*i, 0) + (elf*11)
    lowh = elf if presents[elf] >= INPUT else -1
    del presents[elf]
    elf += 1
print("Day 20: Answer Part 2:", lowh)
