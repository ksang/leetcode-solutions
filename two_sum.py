class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = {}
        for i,n in enumerate(nums):
            if d.has_key(target - n):
                return [d[target-n], i+1]
            else:
                d[n] = i+1

if __name__ == '__main__':
    Solution().twoSum([2,7,11,15], 9)