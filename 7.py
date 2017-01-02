# import sys
# inputdata = sys.stdin.readlines()

# data = [x.rstrip('\n') for x in inputdata]

# import re

# prog_0 = re.compile(r'^(\d*|\w*) -> (\w*)$')
# prog_1 = re.compile(r'^(NOT) (\d*|\w*) -> (\w*)$')
# prog_2 = re.compile(r'^(\d*|\w*) (AND|OR|LSHIFT|RSHIFT) (\d*|\w*) -> (\w*)$')

# def resolve(f):
#     r = resolve(f)
#     if callable(r):
#         return resolve(r)
#     return r

# def handle_0(wires, x, o):
#     xv = lambda: resolve(wires[x]) if x.isalpha() else int(x)
#     wires[o] = xv

# def handle_1(wires, x, op, o):
#     xv = lambda: resolve(wires[x]) if x.isalpha() else int(x)
#     if op == 'NOT':
#         wires[o] = lambda: ~xv()
#     else:
#         print "UNHANDLED!!!"

# def handle_2(wires, x, y, op, o):
#     xv = lambda: wires[x] if x.isalpha() else int(x)
#     yv = lambda: wires[y] if y.isalpha() else int(y)
#     if op == 'AND':
#         wires[o] = lambda: xv() & yv()
#     elif op == 'OR':
#         wires[o] = lambda: xv() | yv()
#     elif op == 'LSHIFT':
#         wires[o] = lambda: xv() << yv()
#     elif op == 'RSHIFT':
#         wires[o] = lambda: xv() >> yv()
#     else:
#         print "UNHANDLED!!!"

# from collections import defaultdict
# wires = defaultdict(int)

# for d in data:
#     handled = False
#     m = prog_0.match(d)
#     if m:
#         x = m.group(1)
#         o = m.group(2)

#         handle_0(wires, x, o)

#     m = prog_1.match(d)
#     if m:
#         x  = m.group(2)
#         o  = m.group(3)
#         op = m.group(1)

#         handle_1(wires, x, op, o)

#     m = prog_2.match(d)
#     if m:
#         x  = m.group(1)
#         y  = m.group(3)
#         o  = m.group(4)
#         op = m.group(2)

#         handle_2(wires, x, y, op, o)

# print wires['a']()


import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re

prog_0 = re.compile(r'^(\d*|\w*) -> (\w*)$')
prog_1 = re.compile(r'^(NOT) (\d*|\w*) -> (\w*)$')
prog_2 = re.compile(r'^(\d*|\w*) (AND|OR|LSHIFT|RSHIFT) (\d*|\w*) -> (\w*)$')

def handle_0(wires, x, o):
    if not x.isalpha():
        wires[o] = int(x)
    else:
        if x in wires:
            wires[o] = wires[x]

def handle_1(wires, x, op, o):
    if op == 'NOT':
        f = lambda p1: ~p1
    else:
        print "UNHANDLED!!!"
        return

    if not x.isalpha():
        wires[o] = f(int(x))
    else:
        if x in wires:
            wires[o] = f(wires[x])

def handle_2(wires, x, y, op, o):
    if op == 'AND':
        f = lambda p1,p2: p1 & p2
    elif op == 'OR':
        f = lambda p1,p2: p1 | p2
    elif op == 'LSHIFT':
        f = lambda p1,p2: p1 << p2
    elif op == 'RSHIFT':
        f = lambda p1,p2: p1 >> p2
    else:
        print "UNHANDLED!!!"
        return

    if not x.isalpha():
        xv = int(x)
    else:
        if x in wires:
            xv = wires[x]
        else:
            return

    if not y.isalpha():
        yv = int(y)
    else:
        if y in wires:
            yv = wires[y]
        else:
            return

    wires[o] = f(xv, yv)

wires = {}

while not 'a' in wires:
    for d in data:
        m = prog_0.match(d)
        if m:
            x = m.group(1)
            o = m.group(2)

            handle_0(wires, x, o)

        m = prog_1.match(d)
        if m:
            x  = m.group(2)
            o  = m.group(3)
            op = m.group(1)

            handle_1(wires, x, op, o)

        m = prog_2.match(d)
        if m:
            x  = m.group(1)
            y  = m.group(3)
            o  = m.group(4)
            op = m.group(2)

            handle_2(wires, x, y, op, o)

print wires['a']