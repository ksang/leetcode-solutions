import sys
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def overflow(self, v):
        if v > 2147483647:
            return 2147483647
        if v < -2147483648:
            return -2147483648
        return v

    def divide(self, dividend, divisor):
        sign = 1
        if dividend < 0:
            sign = -1
            dividend *= -1
        if divisor < 0:
            sign *= -1
            divisor *= -1
        res = 0
        q = dividend
        d = 1
        while True:
            q = q - d*divisor
            if q > 0:
                res += d
                d = d*2
            elif q == 0:
                res += d
                return self.overflow(sign*res)
            else:
                if d == 1:
                    return self.overflow(sign*res)
                else:
                    q += d*divisor
                    d = 1

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "input dividend and divisor"
        sys.exit(0)
    print Solution().divide(int(sys.argv[1]), int(sys.argv[2]))
