def read_gates():
    with open('day07.txt') as f:
        lines = f.readlines()
    gates = {}
    for line in lines:
        gate = line.strip()
        parts = gate.split(' ')
        key = parts[-1]
        parts = [p if p.isnumeric() else "{%s}" % p for p in parts]
        if 'NOT' in gate:
            gates[key] = "(~%s & 0xFFFF)" % parts[1]
        elif 'AND' in gate:
            gates[key] = "(%s & %s)" % (parts[0], parts[2])
        elif 'OR' in gate:
            gates[key] = "(%s | %s)" % (parts[0], parts[2])
        elif 'LSHIFT' in gate:
            gates[key] = "(%s << %s)" % (parts[0], parts[2])
        elif 'RSHIFT' in gate:
            gates[key] = "(%s >> %s)" % (parts[0], parts[2])
        else:
            gates[key] = parts[0]
    return gates


def process_gates(gates):
    while '{' in gates['a']:
        key = [k for k, v in gates.items() if v.isnumeric()][0]
        t = "{%s}" % key
        for k, v in gates.items():
            if t in v:
                v_new = v.replace(t, gates[key])
                try:
                    gates[k] = str(eval(v_new))
                except (NameError, TypeError, SyntaxError):
                    gates[k] = v_new
        del gates[key]
    return gates['a']


gates = read_gates()
val_a = process_gates(gates)
print("Day 07: Answer Part 1:", val_a)
gates = read_gates()
gates['b'] = val_a
val_a = process_gates(gates)
print("Day 07: Answer Part 2:", val_a)
