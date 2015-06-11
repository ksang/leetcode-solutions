import math

class Solution:
    # @param {integer} x
    # @return {boolean}
    def get_digit_number(self, x):
        if x == 0:
            return 1
        else: return int(math.log(x,10)) + 1

    def isPalindrome(self, x):
        if x < 0:
            return False
        n = self.get_digit_number(x)
        if n == 1:
            return True
        for i in range(1, n/2+1):
            c1 = (x % pow(10,i))/pow(10,i-1)
            c2 = (x/pow(10,n-i)) % 10
            if c1 != c2:
                return False
        return True

if __name__ == '__main__':
    print Solution().isPalindrome(123123)
    print Solution().isPalindrome(123321)
    print Solution().isPalindrome(1234321)
    print Solution().isPalindrome(1)