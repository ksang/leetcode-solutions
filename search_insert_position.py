class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def si(self, nums, target, start, end):
        if start > end:
            return min(start,end)+1
        mid = (start+end)/2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.si(nums,target,start,mid-1)
        else:
            return self.si(nums,target,mid+1,end) 

    def searchInsert(self, nums, target):
        return self.si(nums,target,0,len(nums)-1)

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6],2)