class Solution(object):
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		res = [0]*(num+1)
		if num < 1:
			return res
		i = 2
		res[1] = 1
		while i <= num:
			j = 0
			p = i
			while i <= min(num, p*2-1):
				res[i] = res[j] + 1
				i += 1
				j += 1
		return res

if __name__ == '__main__':
	print Solution().countBits(16)