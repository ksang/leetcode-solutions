class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        count = len(nums)
        last = float("inf")
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                count -= 1
            else: i += 1
        return count

if __name__ == '__main__':
    print Solution().removeDuplicates([1,1,2,2])