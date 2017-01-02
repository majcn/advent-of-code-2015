import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]
data = map(int, data)
data = set(data)

NR_GROUPS = 4
wPerGroup = sum(data) / NR_GROUPS


from itertools import combinations

def gGenerator(s, sort=False):
    for counter in range(1, len(s) + 1):
        cc = [c for c in combinations(s, counter) if sum(c) == wPerGroup]
        if sort:
            cc = sorted(cc, key=lambda x: reduce(lambda e,r: r*e, x))
        for c in cc:
            yield c

for g1 in gGenerator(data, True):
    go = data - set(g1)
    for g2 in gGenerator(go):
        goo = go - set(g2)
        for g3 in gGenerator(goo):
            g4 = goo - set(g3)
            if sum(g4) == wPerGroup:
                print reduce(lambda x,r: x*r, g1)
                sys.exit(0)
