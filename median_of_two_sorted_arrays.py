class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def med_idx(self, size):
        if size == 1:
            return 0
        else:
            if size % 2 == 0:
                return size/2-1
            else:
                return size/2

    def get_median(self, array):
        size = len(array)
        if size % 2 == 0:
            pos = size/2-1
            return float(array[pos]+array[pos+1])/2
        else:
            pos = size/2
            return float(array[pos])

    def smaller_than(self, a1, a2, i1, i2):
        if i2 >= len(a2):
            return True
        if i1 < len(a1):
            if a1[i1] <= a2[i2]:
                return True
        else:
            return False

    def findMedianSortedArrays(self, nums1, nums2):
        size_1 = len(nums1)
        size_2 = len(nums2)
        if (size_1+size_2) % 2 == 0:
            pos1 = (size_1+size_2)/2-1
            pos2 = pos1+1
        else:
            pos1 = pos2 = (size_1+size_2)/2

        if size_1 == 0:
            return self.get_median(nums2)
        if size_2 == 0:
            return self.get_median(nums1)

        median_1 = self.get_median(nums1)
        median_2 = self.get_median(nums2)

        if median_1 == median_2:
            return median_1
        elif median_1 < median_2:
            a1 = nums1
            i1 = self.med_idx(size_1)
            a2 = nums2
        else:
            a1 = nums2
            i1 = self.med_idx(size_2)
            a2 = nums1

        k = i1
        i = i1
        j = 0

        res = []
        while True:
            if self.smaller_than(a1, a2, i, j):
                val = a1[i]
                if i <= len(a1)-1:
                    i+=1
            else:
                val = a2[j]
                if j <= len(a2)-1:
                    j+=1
            if k == pos1:
                res.append(val)
            if k == pos2:
                res.append(val)
                print res
                return float(res[0]+res[1])/2
            k+=1
        



if __name__ == '__main__':
    n1 = [100000]
    n2 = [100001]
    print Solution().findMedianSortedArrays(n1,n2)