class Solution:
    # @param {string} str
    # @return {integer}
    def checkoverflow(self, i):
        if i > 2147483647:
            return 2147483647
        if i < -2147483648:
            return -2147483648
        return i
        
    def myAtoi(self, str):
        res = ''
        sign = ''
        s = str.strip()
        if len(s) == 0:
            return 0
        else:
            if s[0] == '-':
                sign = '-'
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
            for c in s:
                if c.isdigit():
                    res += c
                else:
                    break
            if len(res) == 0:
                return 0
            else:
                return self.checkoverflow(int(sign + res))

if __name__ == '__main__':
    print Solution().myAtoi('')
    print Solution().myAtoi('--123321')
    print Solution().myAtoi('-221a34')