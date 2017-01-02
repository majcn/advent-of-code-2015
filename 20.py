INPUT = 29000000


houses = [0 for i in range(1000000)]
maxElfs = INPUT / 10
for i in range(1, maxElfs):
    housei = i
    while housei < len(houses):
        houses[housei] += i*10
        housei += i
print next(i for i in range(len(houses)) if houses[i] >= INPUT)


houses = [0 for i in range(1000000)]
maxElfs = INPUT / 10
for i in range(1, maxElfs):
    housei = i
    while housei < len(houses) and housei / i <= 50:
        houses[housei] += i*11
        housei += i
print next(i for i in range(len(houses)) if houses[i] >= INPUT)
