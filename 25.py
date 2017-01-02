import sys
from itertools import count

R = 2978 - 1
C = 3083 - 1

def generator(start):
    p = start
    for x in count(1):
        for y in range(x+1):
            p = p * 252533 % 33554393
            yield (x-y, y, p)

g = generator(20151125)

print next(p for x,y,p in generator(20151125) if x == R and y == C)
# while True:
#     x, y, p = g.next()
#     if x == R and y == C:


# R = 9
# C = 9

# codes = [[0]*C for i in range(R)]

# p = 20151125
# codes[0][0] = p

# for x in range(1, R):
#     for y in range(x+1):
#         p = p * 252533 % 33554393
#         codes[x-y][y] = p

# for c in codes:
#     print c

# # print codes[0][1]