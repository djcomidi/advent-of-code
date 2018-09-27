
PLAIN = 0
MARKER_READ = 1
MARKER_REPEAT = 2
MARKER_DATA = 3

with open('day09.txt') as f:
    data = f.read().strip()

state = PLAIN
m_len, m_repeat = 0, 0
message, word = "", ""
for c in data:
    if c == ' ': continue
    if state == PLAIN:
        if c == '(':
            state = MARKER_READ
        else:
            message += c
    if state == MARKER_READ:
        if c == '(':
            m_len, m_repeat, word = 0, 0, ""
        elif c == 'x':
            state = MARKER_REPEAT
        else:
            m_len = (10 * m_len) + int(c)
    elif state == MARKER_REPEAT:
        if c == ')':
            state = MARKER_DATA
        else:
            m_repeat = (10 * m_repeat) + int(c)
    elif state == MARKER_DATA:
        if m_len > 0:
            word += c
            m_len -= 1
        if m_len == 0:
            message += word * m_repeat
            m_len, m_repeat = 0, 0
            state = PLAIN

print("Day 09: Answer Part 1:", len(message))
