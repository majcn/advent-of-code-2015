import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

import re
prog_hlf = re.compile(r'^hlf (a|b)$')
prog_tpl = re.compile(r'^tpl (a|b)$')
prog_inc = re.compile(r'^inc (a|b)$')
prog_jmp = re.compile(r'^jmp ([+-]\d+)$')
prog_jie = re.compile(r'^jie (a|b), ([+-]\d+)$')
prog_jio = re.compile(r'^jio (a|b), ([+-]\d+)$')

def handle_hlf(state, r):
    registers = state[1]
    registers[r] = registers[r] / 2

def handle_tpl(state, r):
    registers = state[1]
    registers[r] = registers[r] * 3

def handle_inc(state, r):
    registers = state[1]
    registers[r] = registers[r] + 1

def handle_jmp(state, offset):
    offset = int(offset)
    state[0] = state[0] + offset - 1

def handle_jie(state, r, offset):
    registers = state[1]
    if registers[r] % 2 == 0:
        handle_jmp(state, offset)

def handle_jio(state, r, offset):
    registers = state[1]
    if registers[r] == 1:
        handle_jmp(state, offset)

def handleCommand(c, d):
    m = c[0].match(d)
    if m:
        return (m.groups(), c[1])
    return None

commands = [
    (prog_hlf, handle_hlf),
    (prog_tpl, handle_tpl),
    (prog_inc, handle_inc),
    (prog_jmp, handle_jmp),
    (prog_jie, handle_jie),
    (prog_jio, handle_jio)
]

prog = [filter(None, [handleCommand(c, d) for c in commands])[0] for d in data]
for a in [0, 1]:
    state = [0, {'a': a, 'b': 0}]
    while state[0] < len(prog):
        p = prog[state[0]]
        p[1](state, *p[0])
        state[0] += 1

    print state[1]['b']