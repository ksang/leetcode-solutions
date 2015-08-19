import sys
class Solution:
    # @param {integer} n
    # @return {string}
    def count(self, s):
        p = s[0]
        count = 1
        res = ''
        for c in s[1:]:
            if c == p:
                count+=1
            else:
                res += str(count) + p
                p = c
                count = 1
        res += str(count) + p
        return res

    def gen(self):
        r = '1'
        while  True:
            r = self.count(r)
            yield r

    def countAndSay(self, n):
        if n == 1:
            return '1'
        g = self.gen()
        for i in range(1,n):
            res = g.next()
        return res

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please input integer"
    else:
        print Solution().countAndSay(int(sys.argv[1]))
