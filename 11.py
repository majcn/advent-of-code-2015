INPUT = 'hepxcrrq'

def nextPassword(password, off=1):
    offc = password[-off]
    if offc != 'z':
        return password[:-off] + chr(ord(offc) + 1) + ((off-1) * 'a')
    else:
        return nextPassword(password, off + 1)

def isValid(password):
    if any(i in password for i in 'iol'):
        return False

    if len({password[i:i+2] for i in range(len(password) - 1) if password[i] == password[i+1]}) <= 1:
        return False

    if any(password[i:i+3] == password[i] + chr(ord(password[i]) + 1) + chr(ord(password[i]) + 2) for i in range(len(password) - 2)):
        return True

    return False

def passwordGenerator(password):
    while True:
        password = nextPassword(password)
        if isValid(password):
            yield password

g = passwordGenerator(INPUT)
print g.next()
print g.next()
