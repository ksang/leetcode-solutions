class Solution(object):
	def minPatches(self, nums, n):
		"""
		:type nums: List[int]
		:type n: int
		:rtype: int
		"""
		res = 0
		cover = 0
		next = 1
		i = 0
		while cover < n:
			if i < len(nums):
				if next < nums[i]:
					res += 1
					cover += next
				else:
					cover += nums[i]
					i += 1
				next = cover + 1
			else:
				cover += cover + 1
				res += 1
		return res

if __name__ == '__main__':
	print Solution().minPatches([1,3],2147483647)