INPUT = '1113122113'

from itertools import groupby

d = INPUT
for i in range(50):
    r = ''
    for x in groupby(d):
        r += str(len(list(x[1]))) + x[0]
    d = r

print len(d)