import sys
class Solution:
    # @param {integer} n
    # @return {string[]}
    def complete(self, prefix, res):
        i = 0
        for c in prefix:
            if c == '(':i += 1
            else: i -= 1
        res.append(prefix+(i*')'))  

    def gen_combi(self, prefix, n, res):
        if n > 0:
            self.gen_combi(prefix+'(',n-1,res)
            i = 0
            for c in prefix:
                if c == '(': i += 1
                else: i -= 1
            if i > 0:
                self.gen_combi(prefix+')',n,res)
        else:
            self.complete(prefix,res)

    def generateParenthesis(self, n):
        res = []
        self.gen_combi('(', n-1, res)
        return res

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please input a number to generate parentheses."
        sys.exit(0)
    print Solution().generateParenthesis(int(sys.argv[1]))