from math import floor
from math import ceil

def swap(i, j, nums):
	buf = nums[j]
	nums[j] = nums[i]
	nums[i] = buf

# group list to two parts, greater than / less than nums[pivotIndex]
def partition(nums, left, right, pivotIndex):
	pivotValue = nums[pivotIndex]
	swap(pivotIndex, right, nums)
	storeIndex = left
	for i in range(left, right):
		if nums[i] < pivotValue:
			swap(storeIndex, i, nums)
			storeIndex += 1
	# move pivot to it's final place
	swap(right, storeIndex, nums)
	return storeIndex

# implement with insertion sort
def partition5(nums, left, right):
	buf = []
	for i in range(left, right+1):
		buf.append((nums[i], i))
	for i in range(0, len(buf)):
		j = i
		while j > 0 and buf[j][0] < buf[j-1][0]:
			swap(j-1, j, buf)
			j -= 1
	return buf[len(buf)/2][1]

def pivot(nums, left, right):
	if right - left < 5:
		return partition5(nums, left, right)
	i = left
	while i < right:
		subRight = i + 4
		if subRight > right:
			subRight = right
		median5 = partition5(nums, i, subRight)
		swap(median5, int(left + floor((i - left)/5)), nums)
		i += 5
	return select(nums, left, int(left + ceil((right - left)/5) - 1), left + (right - left)/10)

def select(nums, left, right, n):
	if left == right:
		return left
	while True:
		pivotIndex = pivot(nums, left, right)
		pivotIndex = partition(nums, left, right, pivotIndex)
		if n == pivotIndex:
			return n
		elif n < pivotIndex:
			right = pivotIndex - 1
		else:
			left = pivotIndex + 1

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
		median = nums[select(nums, 0, self.n-1, (self.n-1)/2)]
		i = j = 0
		k = self.n-1
		while j < k:
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
	nums = [1,3,2,2,3,1]
	Solution().wiggleSort(nums)
	print nums


