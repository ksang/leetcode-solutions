import sys

class Solution:
    # @param {string} s
    # @return {integer}
    def concatenate(self,pl):
        if len(pl) == 0: return []
        res = []
        start = pl[0][0]
        end = pl[0][1]
        i = 0
        while i < len(pl)-1:
            if pl[i][1] == pl[i+1][0]-1:
                end = pl[i+1][1]
            else:
                res.append([start,end])
                start = pl[i+1][0]
                end = pl[i+1][1]
            i += 1
        res.append([start,end])
        return res

    def lvp(self,s,pl):
        if len(pl) == 0:
            #first round
            i = 0
            start = end = -1
            while i < len(s)-1:
                if s[i] == '(':
                    if s[i+1] == ')':
                        j = i+2
                        while j < len(s)-1:
                            if s[j] == '(' and s[j+1] == ')':
                                j+=2
                            else:
                                break
                        pl.append([i,j-1])
                        i=j-1
                i+=1
            if len(pl) > 0:
                return self.lvp(s,pl)
            else: return []
        else:
            has_new = False
            for p in pl:
                while p[0]-1 >=0 and p[1]+1 <= len(s)-1:
                    if s[p[0]-1] == '(' and s[p[1]+1] == ')':
                        p[0] -= 1
                        p[1] += 1
                        has_new = True
                    else: break
            if has_new:
                pl = self.concatenate(pl)
                return self.lvp(s,pl)
            else:
                # nothing added, return
                return pl

    def longestValidParentheses(self, s):
        pl = []
        res = self.lvp(s,pl)
        #print res
        ans = 0
        for r in res:
            ans = max(ans,r[1]-r[0]+1)
        return ans

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please provide parentheses pattern"
        sys.exit(0)
    print Solution().longestValidParentheses(sys.argv[1])