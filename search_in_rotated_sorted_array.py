class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def bin_search(self, nums, key, start, end):
        if start > end:
            return -1
        mid = (start+end)/2
        if nums[start] < nums[end]:
            # no pivot
            if key == nums[mid]:
                return mid
            elif key < nums[mid]:
                return self.bin_search(nums, key, start, mid-1)
            else:
                return self.bin_search(nums, key, mid+1, end)
        else:
            if nums[mid] < nums[end]:
                # pivot is on the left side:
                if key == nums[mid]:
                    return mid
                elif key < nums[mid]:
                    return self.bin_search(nums, key, start, mid-1)
                else:
                    if key <= nums[end]:
                        return self.bin_search(nums, key, mid+1, end)
                    else:
                        return self.bin_search(nums, key, start, mid-1)
            else:
                # pivot is on the right side:
                if key == nums[mid]:
                    return mid
                elif key < nums[mid]:
                    if key >= nums[start]:
                        return self.bin_search(nums, key, start, mid-1)
                    else:
                        return self.bin_search(nums, key, mid+1, end)
                else:
                    return self.bin_search(nums, key, mid+1, end)

    def search(self, nums, target):
        return self.bin_search(nums, target, 0, len(nums)-1)

if __name__ == '__main__':
    print Solution().srsa([4,5,6,7,0,1,2],100)