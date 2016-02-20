items_per_column = 15

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

def find_i_th_smallest( A, i ):
    t = len(A)
    if(t <= items_per_column):
        # if A is a small list with less than items_per_column items, then:
        #     1. do sort on A
        #     2. return the i-th smallest item of A
        #
        return sorted(A)[i]
    else:
        # 1. partition A into columns of items_per_column items each. items_per_column is odd, say 15.
        # 2. find the median of every column
        # 3. put all medians in a new list, say, B
        #
        B = [ find_i_th_smallest(k, (len(k) - 1)/2) for k in [A[j:(j + items_per_column)] for j in range(0,len(A),items_per_column)]]

        # 4. find M, the median of B
        #
        M = find_i_th_smallest(B, (len(B) - 1)/2)

        # 5. split A into 3 parts by M, { < M }, { == M }, and { > M }
        # 6. find which above set has A's i-th smallest, recursively.
        #
        P1 = [ j for j in A if j < M ]
        if(i < len(P1)):
            return find_i_th_smallest( P1, i)
        P3 = [ j for j in A if j > M ]
        L3 = len(P3)
        if(i < (t - L3)):
            return M
        return find_i_th_smallest( P3, i - (t - L3))

class Solution(object):
	# vIndex: 1 3 5 7 9 0 2 4 6 8
	def vIndex(self, i):
		return (1+2*i) % (self.n|1)

	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		self.n = len(nums)
		if self.n <= 1:
			return
		median = find_i_th_smallest(nums, (self.n-1)/2)
		print median
		i = j = 0
		k = self.n-1
		while j <= k:
			if nums[self.vIndex(j)] > median:
				swap(self.vIndex(i),self.vIndex(j),nums)
				i += 1
				j += 1
			elif nums[self.vIndex(j)] < median:
				swap(self.vIndex(k),self.vIndex(j),nums)
				k -= 1
			else:
				j += 1


if __name__ == '__main__':
	nums = [1,5,1,1,6,4]
	Solution().wiggleSort(nums)
	print nums


