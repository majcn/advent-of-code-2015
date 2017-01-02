import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

def nextLocation(l, d):
    return { '^': (l[0], l[1] - 1), 'v': (l[0], l[1] + 1), '<': (l[0] - 1, l[1]), '>': (l[0] + 1, l[1]) }[d]


from collections import defaultdict
locs = defaultdict(int)
l = (0, 0)
locs[l] += 1
for d in data[0]:
    l = nextLocation(l, d)
    locs[l] += 1

print len(locs.values())




from collections import defaultdict
locs = defaultdict(int)
lS = (0, 0)
lR = (0, 0)
locs[lS] += 1
locs[lR] += 1
for i, d in enumerate(data[0]):
    if i % 2 == 0:
        lR = nextLocation(lR, d)
        locs[lR] += 1
    else :
        lS = nextLocation(lS, d)
        locs[lS] += 1

print len(locs.values())
