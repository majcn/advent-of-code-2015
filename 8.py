import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re

print reduce(lambda r, x: r + len(x) - (len(re.sub(r'(\\x..)', '1', x.replace('\\\\', '1').replace('\\"', '1'))) - 2), data, 0)
print reduce(lambda r, x: r + (len(x.replace('"', '11').replace('\\', '11')) + 2) - len(x), data, 0)
