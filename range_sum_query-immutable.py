class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums) < 1:
            return
        self.cnums = [0]
        c = nums[0]
        self.cnums.append(c)
        for idx in range(1, len(nums)):
            c += nums[idx]
            self.cnums.append(c)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cnums[j+1] - self.cnums[i]
        
if __name__ == '__main__':
    data = [-2,0,3,-5,2,-1]
    s = NumArray(data)
    #print s.sumRange(0,2)
    print s.sumRange(2,5)
    print s.sumRange(0,5)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)