class Solution(object):
	def maxNumber(self, nums1, nums2, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[int]
		"""
		res = []

		def dfs(nums1, nums2, k, res):
			if k <= 0:
				return
			m, n = len(nums1), len(nums2)
			max1 = max2 = max1o = max2o = 0
			m1 = m2 = 0
			for i in range(0, min(m+n-k+1, m)):
				if nums1[i] > max1:
					max1o = max1
					max1 = nums1[i]
					m1 = i
			for i in range(0, min(m+n-k+1, n)):
				if nums2[i] > max2:
					max2o = max1
					max2 = nums2[i]
					m2 = i
			if max1 == max2:
				if max1o > max2o:
					max1 += 1
				elif max1o < max2o:
					max1 -= 1
			if max1 >= max2:
				res.append(max1)
				dfs(nums1[m1+1:], nums2, k-1, res)
			else:
				res.append(max2)
				dfs(nums1, nums2[m2+1:], k-1, res)

		dfs(nums1, nums2, k, res)

		return res

if __name__ == "__main__":
	nums1 = [6,7]
	nums2 = [6,0,4]
	k = 5
	print Solution().maxNumber(nums1,nums2,k)

