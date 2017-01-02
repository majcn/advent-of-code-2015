import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

def strToElements(s):
    r = []
    for c in s:
        if c.islower():
            r[-1] +=c
        else:
            r.append(c)
    return r

sCodes = {
    'Mg': 'A',
    'B':  'B',
    'F':  'C',
    'H':  'D',
    'C':  'E',
    'O':  'F',
    'N':  'G',
    'P':  'H',
    'Si': 'I',
    'Th': 'J',
    'Ti': 'K',
    'Y':  'L',
    'Rn': 'M',
    'e':  'N',
    'Ca': 'O',
    'Al': 'P',
    'Ar': 'Q'
}

from collections import defaultdict
replacements = defaultdict(list)
for d in data[:-2]:
    x, y = d.split(' => ')

    xx = sCodes[x]
    yy = ''.join([sCodes[ey] for ey in strToElements(y)])

    replacements[xx].append(yy)




START = ''.join(sCodes[x] for x in strToElements(data[-1]))
GOAL = sCodes['e']

# part 1
cMolecules = set()
molecule = START
for i in range(len(molecule)):
    m = molecule[i]
    if m in replacements:
        p1 = molecule[:i]
        p2 = molecule[(i+1):]
        for r in replacements[m]:
            cMolecules.add(p1 + r + p2)

print len(cMolecules)


# part 2
import heapq
priorityQueue = [(len(START), (0, START))]

while priorityQueue:
    it, current = heapq.heappop(priorityQueue)[1]
    lcurrent = len(current)

    if current == GOAL:
        print it
        break

    for kr, vr in replacements.items():
        for r in vr:
            i = current.find(r)
            if i != -1:
                nextIt = it + 1
                nextEl = current[:i] + kr + current[(i+len(r)):]
                heapq.heappush(priorityQueue, (len(nextEl), (nextIt, nextEl)))
