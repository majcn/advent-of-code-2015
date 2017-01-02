import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

lights = [[l == '#' for l in d] for d in data]
SIZE = 100
STEPS = 100

def nextState(lights):
    nbs = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

    newLights = [[False] * SIZE for i in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            nOn = 0
            for n in nbs:
                x = i + n[0]
                y = j + n[1]
                if x >= 0 and x < SIZE and y >= 0 and y < SIZE:
                    nOn += lights[x][y]
            newLights[i][j] = nOn == 3 or nOn == 2 if lights[i][j] else nOn == 3
    return newLights

def part2(lights):
    lights[0][0]   = True
    lights[0][-1]  = True
    lights[-1][0]  = True
    lights[-1][-1] = True
    return lights

lights = part2(lights)
for i in range(STEPS):
    lights = part2(nextState(lights))

print sum(map(sum, lights))
