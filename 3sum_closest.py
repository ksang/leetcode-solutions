class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def get_abs(self, num):
        if num >= 0: return num
        else: return -num

    def threeSumClosest(self, nums, target):
        if len(nums) < 3: return
        nums.sort()
        ret = float('inf')
        for i in range(0, len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                cur = nums[i]+nums[left]+nums[right]
                if self.get_abs(cur-target) < self.get_abs(ret-target):
                    ret = cur
                if cur > target:
                    right -= 1
                    while right > left and nums[right] == nums[right+1]: right -= 1
                elif cur < target:
                    left += 1
                    while right > left and nums[left] == nums[left-1]: left += 1
                else:
                    return ret
        return ret

if __name__ == '__main__':
    print Solution().threeSumClosest([-1,2,1,4],1)