import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

print map(lambda d: sum(1 if c == '(' else -1 for c in d), data)

s = 0
for i, c in enumerate(data[0]):
    s += (1 if c == '(' else -1)
    if s == -1:
        print i + 1
        break
