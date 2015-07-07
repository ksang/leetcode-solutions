class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if len(nums) == 0: return
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else: i += 1
        return len(nums)

if __name__ == '__main__':
    nums = [1,2,2,2,4,5]
    print Solution().removeElement(nums,2)
    print nums