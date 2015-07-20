class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    #https://en.wikipedia.org/wiki/Permutation
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def nextPermutation(self, nums):
        if len(nums) <= 1: return
        i = 0
        k = -1
        # Find the largest index k such that nums[k] < nums[k + 1]
        while i <= len(nums)-2:
            if nums[i] < nums[i+1]:
                k = i
            i += 1
        # array in reverse order
        if k == -1:
            nums.reverse()
            return
        l = -1
        j = k+1
        # Find the largest index l greater than k such that nums[k] < nums[l]
        while j <= len(nums)-1:
            if nums[k] < nums[j]:
                l = j
            j += 1
        # swap nums[k] with nums[l]
        self.swap(nums, k, l)
        i = k+1
        j = len(nums)-1
        while i < j:
            self.swap(nums,i,j)
            i += 1
            j -= 1

if __name__ == '__main__':
    n = [1,3,2]
    Solution().nextPermutation(n)
    print n