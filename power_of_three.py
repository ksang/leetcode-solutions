class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 3 or n == 1:
        	return True
        elif n % 3 == 0 and n > 0:
        	return self.isPowerOfThree(n/3)
        else:
        	return False