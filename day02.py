with open('day02.txt') as f:
    lines = f.readlines()

surface, ribbon = 0, 0
for line in lines:
    L, W, H = [int(d.strip(), 10) for d in line.split('x')]
    extra = min(L*W, min(L*H, W*H))
    surface += 2*L*W + 2*L*H + 2*W*H + extra
    maxdim = max(L, max(W, H))
    ribbon += L*W*H + 2 * (L+W+H - maxdim)
print("The total square feet of wrapping paper they should order:", surface)
print("The total feet of ribbon they should order:", ribbon)
