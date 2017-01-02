import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re
prog = re.compile(r'^\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

NR = 100
ingredients = [map(int, prog.match(d).groups()) for d in data]
nrIngredients = len(ingredients)

from itertools import permutations
possibilities = [c for c in permutations(range(NR+1), nrIngredients) if sum(c) == NR]

def getValue(ingredients, p, ii):
    r = sum(p[i] * ingredients[i][ii] for i in range(len(p)))
    return 0 if r < 0 else r

# part 2
possibilities = [p for p in possibilities if getValue(ingredients, p, 4) == 500]

m = 0
for p in possibilities:
    rc = getValue(ingredients, p, 0)
    rd = getValue(ingredients, p, 1)
    rf = getValue(ingredients, p, 2)
    rt = getValue(ingredients, p, 3)

    m = max(m, rc*rd*rf*rt)

print m
