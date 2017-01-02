import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re

prog = re.compile(r'^(\w+) to (\w+) = (\d+)$')

locs = set()
pairs = {}
for d in data:
    l1, l2, d = prog.match(d).groups()
    d = int(d)

    locs.add(l1)
    locs.add(l2)
    pairs[(l1, l2)] = d
    pairs[(l2, l1)] = d

from itertools import permutations
ps = [sum(pairs[(p[i], p[i+1])] for i in range(len(p) - 1)) for p in permutations(locs)]
print min(ps)
print max(ps)
