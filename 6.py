import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

size = 1000
lights = [[0]*size for i in range(size)]

import re

prog_on     = re.compile(r'^turn on (\d+),(\d+) through (\d+),(\d+)$')
prog_off    = re.compile(r'^turn off (\d+),(\d+) through (\d+),(\d+)$')
prog_toggle = re.compile(r'^toggle (\d+),(\d+) through (\d+),(\d+)$')

def handleOn(lights, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            # lights[i][j] = 1
            lights[i][j] += 1

def handleOff(lights, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            # lights[i][j] = 0
            if lights[i][j] > 0:
                lights[i][j] -= 1

def handleToggle(lights, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            # lights[i][j] = (lights[i][j] + 1) % 2
            lights[i][j] += 2

for d in data:
    m = prog_on.match(d)
    if m:
        handleOn(lights, *map(int, m.groups()))

    m = prog_off.match(d)
    if m:
        handleOff(lights, *map(int, m.groups()))

    m = prog_toggle.match(d)
    if m:
        handleToggle(lights, *map(int, m.groups()))

print sum(map(sum, lights))