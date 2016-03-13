class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		m, n = len(word1), len(word2)
		dp = [range(n+1)] + [[i] + n*[0] for i in xrange(1,m+1)]
		for i in xrange(0, m):
			for j in xrange(0, n):
				if word1[i] == word2[j]:
					# character matched no step required
					dp[i+1][j+1] = dp[i][j]
				else:
					# insert	dp[i+1][j+1] = dp[i][j+1] + 1
					# replace	dp[i+1][j+1] = dp[i][j] + 1
					# delete 	dp[i+1][j+1] = dp[i+1][j] + 1
					dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
		return dp[m][n]

if __name__ == '__main__':
	print Solution().minDistance("charge", "exchange")
	#72/115