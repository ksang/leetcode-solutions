class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nd = {}
        res = 0
        for n in nums:
        	nd[n] = True
        while len(nd) > 0:
        	n = nd.iterkeys().next()
        	nd.pop(n)
        	count = 1
        	i = 1
        	while n+i in nd:
        		nd.pop(n+i)
        		i += 1
        		count += 1
        	j = 1
        	while  n-j in nd:
        		nd.pop(n-j)
        		j += 1
        		count += 1
        	res = max(res, count)
        return res

if __name__ == '__main__':
	nums = [1,0,-1]
	print Solution().longestConsecutive(nums)


        