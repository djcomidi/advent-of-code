def run_program(instructions, regA=0, regB=0):
    reg = {"a": regA, "b": regB}
    ip = 0
    while 0 <= ip < len(instructions):
        p = instructions[ip].split(" ")
        if p[0] == "hlf":
            reg[p[-1]] //= 2
            ip += 1
        elif p[0] == "tpl":
            reg[p[-1]] *= 3
            ip += 1
        elif p[0] == "inc":
            reg[p[-1]] += 1
            ip += 1
        elif p[0] == "jmp":
            ip += int(p[1])
        elif p[0] == "jie":
            if reg[p[1][0]] % 2 == 0:
                ip += int(p[2])
            else:
                ip += 1
        elif p[0] == "jio":
            if reg[p[1][0]] == 1:
                ip += int(p[2])
            else:
                ip += 1
    return reg["a"], reg["b"]

with open('day23.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

regA, regB = run_program(instructions)
print("Day 23: Answer Part 1:", regB)
regA, regB = run_program(instructions, regA=1)
print("Day 23: Answer Part 2:", regB)
