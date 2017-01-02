import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re
prog = re.compile(r'^(\d+)x(\d+)x(\d+)$')

def part1(i):
    return 3*i[0]*i[1] + 2*i[1]*i[2] + 2*i[0]*i[2]

def part2(i):
    return 2*i[0] + 2*i[1] + i[0]*i[1]*i[2]

print [sum(f(i) for i in [sorted(map(int, prog.match(d).groups())) for d in data]) for f in [part1, part2]]
