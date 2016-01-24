from hashlib import md5

start = 'bgvyzdsv'
n = 1
while md5((start+str(n)).encode()).hexdigest()[:5] != '00000':
    n += 1
print("Day 04: Answer Part 1:", n)

while md5((start+str(n)).encode()).hexdigest()[:6] != '000000':
    n += 1
print("Day 04: Answer Part 2:", n)
