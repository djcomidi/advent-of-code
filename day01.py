with open('day01.data') as f:
    data = f.read()
level = data.count('(') - data.count(')')
print("The instructions take Santa to floor:", level)

level, pos = 0, 0
for c in data:
    pos += 1
    if c == '(':
        level += 1
    elif c == ')':
        level -= 1
    if level == -1:
        break
print("The position of the character that causes Santa to first enter the basement:", pos)

