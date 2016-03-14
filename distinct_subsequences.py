def print_dp(dp):
	print "="*64
	for d in dp: print d
	print "="*64

class Solution(object):
	def numDistinct(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: int
		"""
		m, n = len(s), len(t)
		dp = [[0 for x in range(m+1)] for x in range(n+1)] 
		for i in range(1,n+1):
			for j in range(1, m+1):
				if i == 1 and t[i-1] == s[j-1]:
					dp[i][j] = dp[i][j-1] + 1
					continue
				# there are two cases:
				# 1. if the new element is not equal, then no new subsequence should be found,
				#	 hence dp[i][j] = dp[i][j-1]
				# 2. if equal, dp[i][j] can be devided into two parts
				#	 a. the new element is on the j position, subsequence number is the prefix number:
				#		dp[i-1][j-1]
				#	 b. the new element is not on the j position, subsequence is the prev number:
				#		dp[i][j-1]
				if t[i-1] == s[j-1]:
					dp[i][j] = dp[i][j-1]+dp[i-1][j-1]
				else:
					dp[i][j] = dp[i][j-1]
			#print_dp(dp)
		return dp[n][m]

if __name__ == '__main__': 
	print Solution().numDistinct("cccbbb", 'cbb')
