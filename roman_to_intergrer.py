import sys

class Solution:
    # @param {string} s
    # @return {integer}
    r2i_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    def romanToInt(self, s):
        i = 0
        ret = 0
        while i < len(s):
            if i >= len(s)-1:
                ret += self.r2i_map[s[i]]
                break
            if self.r2i_map[s[i]] >= self.r2i_map[s[i+1]]:
                ret += self.r2i_map[s[i]]
                i += 1
            else:
                ret += self.r2i_map[s[i+1]]-self.r2i_map[s[i]]
                i += 2
        return ret

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "input roman numeral I - MMMCMXCIX"
        sys.exit(0)
    print Solution().romanToInt(sys.argv[1])