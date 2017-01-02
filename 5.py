import sys
inputdata = sys.stdin.readlines()

data = [x.rstrip('\n') for x in inputdata]

def isNice1(word):
    threevowels  = len([1 for c in word if c in 'aeiou']) >= 3
    doubleLetter = any(word[i] == word[i+1] for i in range(len(word) - 1))
    bannedString = any(word[i:i+2] in ['ab', 'cd', 'pq', 'xy'] for i in range(len(word) - 1))

    return threevowels and doubleLetter and not bannedString

def isNice2(word):
    pairs = [(i, word[i:i+2]) for i in range(len(word) - 1)]
    testPairs = any(p1[1] == p2[1] for p1 in pairs for p2 in pairs if abs(p1[0] - p2[0]) >= 2)
    testBetween = any(word[i] == word[i+2] for i in range(len(word) - 2))

    return testPairs and testBetween


print len([1 for d in data if isNice1(d)])
print len([1 for d in data if isNice2(d)])
