class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def get_next_num(self, nums, i):
        for j in range(i+1, len(nums)):
            if nums[j] != nums[i]:
                return j
        return None

    def threeSum(self, nums):
        if len(nums) <= 2:
            return []
        nums.sort()
        ret = []
        i = 0
        while nums[i] <= 0 and i < len(nums)-2:
            res = [nums[i]]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left += 1
                else:
                    res.extend([nums[left],nums[right]])
                    ret.append(res)
                    res = [nums[i]]
                    right -= 1
                    left = self.get_next_num(nums, left)
                    if left is None: break
            i = self.get_next_num(nums, i)
            if i == None: break
        return ret

if __name__ == '__main__':
    print Solution().threeSum([-1,0,1,2,-1,-4])
    print Solution().threeSum([-1,0,0,0])
    print Solution().threeSum([-2,0,0,2,2])

