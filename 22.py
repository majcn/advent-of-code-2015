def handleMagicMissle(state):
    state[1] -= 53
    state[5] += 53
    state[6] -= 4

def handleDrain(state):
    state[1] -= 73
    state[5] += 73
    state[0] += 2
    state[6] -= 2

def handleShield(state):
    state[1] -= 113
    state[5] += 113
    state[2] = 6

def handlePoison(state):
    state[1] -= 173
    state[5] += 173
    state[3] = 6

def handleRecharge(state):
    state[1] -= 229
    state[5] += 229
    state[4] = 5

def handleTurn(state, spell):
    # part 2
    if state[0] == 1:
        return (False, False)
    state[0] -= 1

    # player turn
    if state[2] > 0:
        state[2] -= 1
    if state[3] > 0:
        state[6] -= 3
        state[3] -= 1
    if state[4] > 0:
        state[1] += 101
        state[4] -= 1

    if state[6] <= 0:
        return (False, True)

    s = spells[spell]
    if not s[1](state):
        return (False, False)

    s[0](state)
    if state[1] < 0:
        return (False, False)

    # boss turn
    if state[2] > 0:
        state[0] += 7
        state[2] -= 1
    if state[3] > 0:
        state[6] -= 3
        state[3] -= 1
    if state[4] > 0:
        state[1] += 101
        state[4] -= 1

    if state[6] <= 0:
        return (False, True)

    state[0] -= BOSS_DMG
    if state[0] <= 0:
        return (False, False)

    return (True, False)



PLAYER_HP    = 50
PLAYER_MP    = 500

BOSS_HP    = 58
BOSS_DMG   = 9

shield_timer   = 0
poison_timer   = 0
recharge_timer = 0
mana_spend = 0

spells = {
    'MagicMissile': [handleMagicMissle, lambda p: True],
    'Drain':        [handleDrain,       lambda p: True],
    'Shield':       [handleShield,      lambda p: p[2] == 0],
    'Poison':       [handlePoison,      lambda p: p[3] == 0],
    'Recharge':     [handleRecharge,    lambda p: p[4] == 0]
}



START = [PLAYER_HP, PLAYER_MP, shield_timer, poison_timer, recharge_timer, mana_spend, BOSS_HP]

import sys
import heapq

wins = []
states = [(0, START)]
minMana = sys.maxint

while states:
    state = heapq.heappop(states)[1]
    for s in spells:
        nstate = list(state)
        t = handleTurn(nstate, s)
        if t[1]:
            print nstate[5]
            sys.exit(0)
        elif t[0]:
            heapq.heappush(states, (nstate[5], nstate))
