class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
        	return False
        i = 1
        mid = 2**31-1
        start = nums[0]
        while i < len(nums)-1:
        	if nums[i] > nums[i-1] or nums[i] > start:
        		mid = min(mid, nums[i])
        		start = min(start, nums[i-1])
        	if nums[i+1] > mid:
        		return True
        	i += 1
        return False

if __name__ == '__main__':
	nums = [5,1,5,5,2,5,4]
	print Solution().increasingTriplet(nums)
