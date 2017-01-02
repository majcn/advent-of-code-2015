import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

from itertools import combinations

r = [len([1 for p in combinations(map(int, data), n) if sum(p) == 150]) for n in range(1, len(data) + 1)]
print sum(r)
print next(x for x in r if x > 0)
