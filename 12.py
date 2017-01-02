import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import json
a = json.loads(data[0])

result = []

def handleList(l):
    for v in l:
        if isinstance(v, dict):
            handleDict(v)
        elif isinstance(v, list):
            handleList(v)
        elif isinstance(v, int):
            result.append(v)

def handleDict(d):
    for v in d.values():
        if v == 'red':
           return

    handleList(d.values())

handleDict(a)
print sum(result)