PLAYER_HP  = 100

BOSS_HP    = 104
BOSS_DMG   = 8
BOSS_ARMOR = 1

weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
armors  = [(0, 0, 0), (13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings   = [(0, 0, 0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

def canDefeatBoss(w,  a, r1, r2):
    dmg   = w[1] + a[1] + r1[1] + r2[1]
    armor = w[2] + a[2] + r1[2] + r2[2]

    dptp = max(1, (dmg - BOSS_ARMOR))
    dptb = max(1, (BOSS_DMG - armor))

    tp = (BOSS_HP   / dptp) + (1 if BOSS_HP   % dptp > 0 else 0)
    tb = (PLAYER_HP / dptb) + (1 if PLAYER_HP % dptb > 0 else 0)

    return tp <= tb

items = None
maxGold = 0
for w in weapons:
    for a in armors:
        for r1 in rings:
            for r2 in rings:
                if not canDefeatBoss(w, a, r1, r2):
                    maxGold = max(maxGold, w[0] + a[0] + r1[0] + r2[0])
print maxGold
