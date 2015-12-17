# TODO: change return type to dictionary {coin type : number required, ...}

class MinimumCoinChange(object):

    def __init__(self):
        self.__coins = ["200", "100", "50", "20", "10", "5", "2", "1"]

    def getMinimumChange(self, amount):
        print(self.getMinimumChangeWorker(amount, self.__coins))

    def getMinimumChangeWorker(self, amount, coins):
        currentMax = int(coins[0])
        currentAmount = amount

        if amount % currentMax == 0:
            return "{1} coins of {0} cents\n" .format(currentMax, (amount // currentMax))

        if amount // currentMax > 0:
            amount -= currentMax * (amount // currentMax)
        return "{1} coins of {0} cents\n".format(currentMax, (currentAmount // currentMax)) + self.getMinimumChangeWorker(amount, coins[1:])


minChange = MinimumCoinChange()
minChange.getMinimumChange(256)