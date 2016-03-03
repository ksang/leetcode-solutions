class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        if len(nodes) % 2 == 0:
        	return False
        if nodes[0] == "#":
        	if len(nodes) == 1:
        		return True
        	else:
        		return False
        stack = ["root"]
        for n in nodes:
        	if n == "#":
        		if stack:
        			stack.pop(-1)
        		else:
        			return False
        	else:
        		stack.append(n)
        if stack:
        	return False
        return True

if __name__ == '__main__':
	print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
