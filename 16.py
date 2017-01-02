import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re
prog = re.compile(r'^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$')

realData = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

aunts = {}
for d in data:
    i, w1, d1, w2, d2, w3, d3 = prog.match(d).groups()
    i, d1, d2, d3 = map(int, [i, d1, d2, d3])
    aunts[i] = { w1: d1, w2: d2, w3: d3 }

def isValid1(aunt):
    global realData

    return not any(1 for r in realData if r in aunt and realData[r] != aunt[r])

def isValid2(aunt):
    global realData

    for r in realData:
        if r in aunt:
            if r in ['cats', 'trees']:
                if realData[r] >= aunt[r]:
                    return False
            elif r in ['pomeranians', 'goldfish']:
                if realData[r] <= aunt[r]:
                    return False
            else:
                if realData[r] != aunt[r]:
                    return False
    return True

print next(i for i, a in aunts.items() if isValid1(a))
print next(i for i, a in aunts.items() if isValid2(a))