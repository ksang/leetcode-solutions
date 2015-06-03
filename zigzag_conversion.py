class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        res = ''
        if numRows == 1:
            return s
        for i in range(1, numRows+1):
            gap = (numRows-1)*2
            gap1 = (numRows-i)*2
            gap2 = gap-gap1
            j = i
            while j <= len(s):
                res += s[j-1]
                j += gap1
                if gap1 > 0 and gap2 > 0 and j <= len(s):
                    res += s[j-1]
                j += gap2
        return res

if __name__ == '__main__':
    print Solution().convert("PAYPALISHIRING", 3)