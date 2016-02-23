class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        check1 = {}
        check2 = {}
        def check(a, b):
        	if check1.has_key(a) and check2.has_key(b):
        		if check1[a] == b and check2[b] == a:
        			return True
        	elif not check1.has_key(a) and not check2.has_key(b):
        		check1[a] = b
        		check2[b] = a
        		return True
        	return False

        sl = str.split(" ")
        if len(pattern) != len(sl): return False
        for i,s in enumerate(sl):
        	if not check(pattern[i], s):
        		return False
        return True

if __name__ == '__main__':
	print Solution().wordPattern("ab", "b c")