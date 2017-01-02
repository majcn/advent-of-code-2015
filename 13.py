import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re
prog = re.compile(r'^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).$')

people = set()
happiness = {}
for d in data:
    p1, gl, h, p2 = prog.match(d).groups()
    h = int(h) * (1 if gl == 'gain' else -1)

    people.add(p1)
    people.add(p2)
    happiness[(p1, p2)] = h

people.add('ME')

from itertools import permutations
def computeHappines(p1, p2):
    if p1 == 'ME' or p2 == 'ME':
        return 0
    return happiness[(p1, p2)] + happiness[(p2, p1)]

print max(sum(computeHappines(p[i], p[i+1]) for i in range(len(p) - 1)) + computeHappines(p[0], p[-1]) for p in permutations(people))
