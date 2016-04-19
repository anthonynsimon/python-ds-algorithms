# TODO: change return type to dictionary {coin type : number required, ...}

class MinimumCoinChange(object):

    def __init__(self):
        self.__coins = ["200", "100", "50", "20", "10", "5", "2", "1"]

    def get_min_change(self, amount):
        print(self.get_min_change_helper(amount, self.__coins))

    def get_min_change_helper(self, amount, coins):
        max = int(coins[0])
        current = amount

        if amount % max == 0:
            return "{1} coins of {0} cents\n" .format(max, (amount // max))

        if amount // max > 0:
            amount -= max * (amount // max)
        return "{1} coins of {0} cents\n".format(max, (current // max)) + self.get_min_change_helper(amount, coins[1:])


minChange = MinimumCoinChange()
minChange.get_min_change(1117)