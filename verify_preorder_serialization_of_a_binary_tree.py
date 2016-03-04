class Solution(object):
	def isValidSerialization(self, preorder):
		"""
		:type preorder: str
		:rtype: bool
		"""
		nodes = preorder.split(",")
		if len(nodes) % 2 == 0:
			return False
		if nodes[-1] != "#":
			return False
		if nodes[0] == "#":
			if len(nodes) == 1:
				return True
			else:
				return False
		stack = [nodes[0]]
		for i in range(1, len(nodes)-1):
			if nodes[i] == "#":
				if stack:
					stack.pop(-1)
				else:
					return False
			else:
				stack.append(nodes[i])
		if stack:
			return False
		return True

if __name__ == '__main__':
	print Solution().isValidSerialization("#")
