class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.interval = []
        m = 0
        while 15 + m*15 < len(nums):
            self.interval.append(self.calcRange(0+m*15, 15+m*15))
            m += 1

    def calcRange(self, i, j):
        res = 0
        while i <= j:
            res += self.nums[i]
            i += 1
        return res

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)