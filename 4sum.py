class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for fidx, fn in enumerate(nums):
            if fn > target/4:
                break
            if fidx >= 1:
                if fn == nums[fidx-1]: continue
            sidx = fidx+1
            while sidx <= len(nums)-3:
                if fn+nums[sidx] > target/2:
                    break
                tidx = sidx+1
                lidx = len(nums)-1
                while tidx < lidx:
                    cn = fn+nums[sidx]+nums[tidx]+nums[lidx]
                    if cn > target:
                        lidx -= 1
                        while tidx < lidx and nums[lidx] == nums[lidx+1]: lidx -= 1
                    elif cn < target:
                        tidx += 1
                        while tidx < lidx and nums[tidx] == nums[tidx-1]: tidx += 1
                    else: 
                        res.append([fn,nums[sidx],nums[tidx],nums[lidx]])
                        tidx += 1
                        while tidx < lidx and nums[tidx] == nums[tidx-1]: tidx += 1                        
                        lidx -= 1
                        while tidx < lidx and nums[lidx] == nums[lidx+1]: lidx -= 1
                sidx += 1
                while sidx <= len(nums)-3 and nums[sidx] == nums[sidx-1]: sidx += 1
        return res
if __name__ == '__main__':
    print Solution().fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9)
    print Solution().fourSum([5,5,5,0,3,2,8,0,0,10,20],10)
