coins = ["200","100","50","20","10","5","2","1"]

def getMinimumChange(n, coins):
    currentMax = int(coins[0])
    print(currentMax, n // currentMax)
    if n % currentMax == 0:
        return "{1} coins of {0} cents\n" .format(currentMax, (n // currentMax))
    currentN = n
    if n // currentMax > 0:
        n -= currentMax * (n // currentMax)
    return "{1} coins of {0} cents\n".format(currentMax, (currentN // currentMax)) + getMinimumChange(n, coins[1:])

print(getMinimumChange(56, coins))