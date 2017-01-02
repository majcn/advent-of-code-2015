import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re
prog = re.compile(r'^\w+ can fly (\d+) km/s for (\d+) seconds?, but then must rest for (\d+) seconds?.$')

players = [map(int, prog.match(d).groups()) for d in data]

time = 2503
path = [0] * len(players)
score = [0] * len(players)

for t in range(time):
    for i, p in enumerate(players):
        if (t % (p[1] + p[2])) < p[1]:
            path[i] += p[0]

    mp = max(path)
    for w in [i for i, x in enumerate(path) if x == mp]:
        score[w] += 1

print max(score)
