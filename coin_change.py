class Solution(object):

    def coin_calc(self, coins, amount, ccount, pos):
        # there is no combination
        if pos < 0:
            return -1
        if coins[pos] > amount:
            self.coin_calc(coins, amount, ccount, pos-1)
        else:
            if amount % coins[pos] == 0:
                return ccount + (amount/coins[pos])
            else:


    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        return coin_calc(coins, amount, 0, len(coins)-1)
        