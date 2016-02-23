class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        i = 3
        while i < len(x):
        	if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
        		print 'case1 ' + str(i)
        		return True
        	if i > 3:
	        	if x[i-1] <= x[i-3] and x[i] + x[i-4] >= x[i-2] and x[i-2] > x[i-4]:
	        		print 'case2 ' + str(i)
	        		return True
        	i += 1
        return False

if __name__ == '__main__':
	x = [1,1,2,2,1,1]
	print Solution().isSelfCrossing(x)