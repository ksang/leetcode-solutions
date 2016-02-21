class Solution(object):

    def coin_calc(self, coins, amount, ccount, pos):
        # there is no combination
        if pos < 0:
            return
        if coins[pos] > amount:
            self.coin_calc(coins, amount, ccount, pos-1)
        else:
            if amount % coins[pos] == 0:
                self.res = min(self.res, ccount + (amount/coins[pos]))
            else:
                print "a:%s pos:%s ccount:%s" % (amount, pos, ccount)
                self.coin_calc(coins, amount%coins[pos], ccount+(amount/coins[pos]), pos-1)
                self.coin_calc(coins, amount, ccount, pos-1)


    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        coins.sort()
        self.res = 2**31-1
        self.coin_calc(coins, amount, 0, len(coins)-1)
        if self.res == 2**31-1:
            return -1
        else:
            return self.res

if __name__ == '__main__':
    coins = [186,419,83,408]
    print Solution().coinChange(coins, 6249)
        