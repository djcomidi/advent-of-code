from pprint import pprint
from functools import lru_cache


# try depth-first and hope it's the right way
def count_min_steps(molecule, depth=0):
    global displacements
    if molecule == "e":
        return depth
    for k, v in displacements:
        i = molecule.rfind(k)
        if i != -1:
            newmol = molecule[:i] + v + molecule[i+len(k):]
            min_steps = count_min_steps(newmol, depth+1)
            if min_steps is not None:
                return min_steps

replacements = dict()
molecule = ""
with open('day19.txt') as f:
    for line in f.readlines():
        ln = line.strip()
        if "=>" in ln:
            molA, _, molB = ln.split(" ")
            replacements[molA] = replacements.get(molA, []) + [molB]
        elif len(ln) > 0:
            molecule = ln

uniques = set()
for k, reps in replacements.items():
    i = molecule.find(k)
    while i > 0:
        for rep in reps:
            uniques.add(molecule[:i] + rep + molecule[i+len(k):])
        i = molecule.find(k, i+1)
print("Day 19: Answer Part 1:", len(uniques))


def keysort(x):
    sign = -1 if any(t in x for t in ["Rn", "Y", "Ar"]) else 1
    return sign * len(x)
displacements = []
for k, reps in replacements.items():
    for rep in reps:
        displacements += [(rep, k)]
displacements = sorted(displacements, key=keysort)
print("Day 19: Answer Part 2:", count_min_steps(molecule))
