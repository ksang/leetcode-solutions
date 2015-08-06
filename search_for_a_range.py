class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def find_l_boundary(self, nums, target, start, end):
        if start > end:
            return
        mid = (start+end)/2
        if nums[mid] == target:
            if mid == 0:
                return 0
            elif nums[mid-1] < target:
                return mid
            else:
                return self.find_l_boundary(nums,target,start,mid-1)
        else:
            return self.find_l_boundary(nums,target,mid+1,end)

    def find_h_boundary(self, nums, target, start, end):
        if start > end:
            return 
        mid = (start+end)/2
        if nums[mid] == target:
            if mid == len(nums)-1:
                return mid
            elif nums[mid+1] > target:
                return mid
            else:
                return self.find_h_boundary(nums,target,mid+1,end)
        else:
            return self.find_h_boundary(nums,target,start,mid-1)

    def sr(self, nums, target, start, end):
        if start > end:
            return [-1,-1]
        mid = (start+end)/2
        if nums[mid] == target:
            start = self.find_l_boundary(nums,target,start,mid-1)
            end = self.find_h_boundary(nums,target,mid+1,end)
            if start is None: start = mid
            if end is None: end = mid
            print "start:%s, end:%s" % (start,end)
            return [start,end]
        elif nums[mid] < target:
            return self.sr(nums,target,mid+1,end)
        else:
            return self.sr(nums,target,start,mid-1)

    def searchRange(self, nums, target):
        return self.sr(nums, target, 0, len(nums)-1)

if __name__ == '__main__':
    print Solution().searchRange([5,7,7,8,8,10],5)