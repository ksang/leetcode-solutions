import sys
class Solution:
    # @param {string} s
    # @return {integer}

    pmap = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    def lvp(self, s, i, j, res):
        print "i:%s, j:%s, res:%s" %(i,j,res)
        if i >= j:
            res[(i,j)] = 0
            return 0
        if res.get((i,j)) is None:
            if s[i] in self.pmap.keys():
                if self.pmap[s[i]] == s[j]:
                    res[(i,j)] = self.lvp(s,i+1,j-1,res)+2
                else:
                    res[(i,j)] = max(self.lvp(s,i+1,j,res),self.lvp(s,i,j-1,res))
            else:
                res[(i,j)] = self.lvp(s,i+1,j,res)
        return res.get((i,j))


    def longestValidParentheses(self, s):
        res = {}
        self.lvp(s,0,len(s)-1,res)
        print res
        return res[(0,len(s)-1)]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please provide parentheses pattern"
        sys.exit(0)
    print Solution().longestValidParentheses(sys.argv[1])