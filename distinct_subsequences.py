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
        		if i > j:
        			dp[i][j] = 0
        		elif t[i-1] == s[j-1]:
        			if dp[i][j-1] != 0:
        				dp[i][j] = dp[i][j-1]+1
        			else:
        		else:
        			dp[i][j] = dp[i][j-1]
        return dp[n][m]

if __name__ == '__main__':
	print Solution().numDistinct("eee", 'eee')
