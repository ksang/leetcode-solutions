class Solution:
    # @param {integer} x
    # @return {integer}
    def check_overflow(self, v):
        if v > 2147483648:
            return 0
        else: return v

    def reverse(self, x):
        s = str(x)
        res = ''
        for i in range(0, len(s)):
            res += s[len(s)-i-1]
        if res[len(s)-1] == '-':
            res = res[:-1]
            return -self.check_overflow(int(res))
        else:
            return self.check_overflow(int(res))

if __name__ == '__main__':
    print Solution().reverse(123)