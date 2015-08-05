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
                print mid
                return mid
            else:
                self.find_l_boundary(nums,target,start,mid-1)
        else:
            self.find_l_boundary(nums,target,mid+1,end)

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
                self.find_h_boundary(nums,target,mid+1,end)
        else:
            self.find_h_boundary(nums,target,start,mid-1)

    def sr(self, nums, target, start, end, rd):
        if start > end:
            rd['start'] = -1
            rd['end'] = -1
            return
        mid = (start+end)/2
        if nums[mid] == target:
            rd['start'] = self.find_l_boundary(nums,target,start,mid-1)
            rd['end'] = self.find_h_boundary(nums,target,mid+1,end) 
            if rd['start'] is None: rd['start']  = mid
            if rd['end'] is None: rd['end'] = mid
            print "left:%s, right:%s" % (rd['start'],rd['end']) 
            return
        elif nums[mid] < target:
            self.sr(nums,target,mid+1,end)
        else:
            self.sr(nums,target,start,mid-1)

    def searchRange(self, nums, target):
        rd = {}
        self.sr(nums, target, 0, len(nums)-1, rd)
        return [rd.get('start'), rd.get('end')]

if __name__ == '__main__':
    print Solution().searchRange([5,7,7,8,8,10],7)