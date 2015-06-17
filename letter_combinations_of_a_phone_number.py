import sys
class Solution:
    # @param {string} digits
    # @return {string[]}
    m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " ",
            "1": ""
    }
    
    def recursive_combi(self, digits, string, res):
        if len(digits) == 0:
            return
        d = digits[0]
        if d == "1":
            self.recursive_combi(digits[1:], string, res)
            return
        for c in self.m[d]:
            if len(digits) == 1:
                res.append(string+c)
            else:
                self.recursive_combi(digits[1:], string+c, res)

    def letterCombinations(self, digits):
        res = []
        self.recursive_combi(digits,'',res)
        return res

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'please input digits'
        sys.exit(0)
    print Solution().letterCombinations(sys.argv[1])
