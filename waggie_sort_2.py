class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
        	return
        i = 0
        j = 1
        while i < len(nums):
        	while j < len(nums):
        		if nums[j] == nums[i]:
        			j += 1
        		else: break
        	buf = nums.pop(j)
        	if nums[i] > nums[j]:
        		if i % 2 == 0:
        			nums.insert(i, buf)
        		else:
        			nums.insert(i+1, buf)
        	else:
        		if i % 2 == 0:
        			nums.insert(i+1, buf)
        		else:
        			nums.insert(i, buf)
        	i += 1

if __name__ == '__main__':
	nums = [3,5,7,1,1,1]
	print Solution().wiggleSort(nums)


