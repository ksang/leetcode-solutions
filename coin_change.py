import time
class Solution(object):

	def __init__(self):
		self.start = time.time()

	def __del__(self):
		print "Time used: %s" % (time.time() - self.start)
	# DFS
	def coinChange(self, coins, amount):
		coins.sort(reverse = True)
		lenc, self.res = len(coins), 2**31-1

		def dfs(pt, rem, count):
			if rem == 0:
				self.res = min(self.res, count)
			for i in range(pt, lenc):
				if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
					dfs(i, rem-coins[i], count+1)

		for i in range(lenc):
			dfs(i, amount, 0)
		return self.res if self.res < 2**31-1 else -1

	# DP
	def coin_change(self, coins, amount):
		coins.sort(reverse = True)
		nums = [2**31-1] * (amount+1)
		nums[0] = 0
		for i in range(1, amount+1):
			for c in coins:
				if c <= i:
					if nums[i-c] != 2**31-1:
						nums[i] = min(nums[i], nums[i-c]+1)
		return nums[amount] if nums[amount] < 2**31-1 else -1

if __name__ == '__main__':
	coins = [370,417,408,156,143,434,168,83,177,280,117]
	print Solution().coinChange(coins, 9953)
	print Solution().coin_change(coins, 9953)
		