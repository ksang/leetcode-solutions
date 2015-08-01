class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}

    def isMatch(self, s, p):
        # Dynamic Programming
        match = [False] * (len(s)+1)
        match[len(s)] = True
        i = len(p)-1
        while i >= 0:
            if p[i] == '*':
                for j in reversed(range(0,len(s))):
                    # two cases indicates a match (set match[j] to true)
                    # 1. the current pos has already be set to true
                    # 2. the * works to match from button to top
                    match[j] = match[j] or (match[j+1] and (p[i-1] == '.' or p[i-1] == s[j]))
                i-=1
            else:
                for j in range(0,len(s)):
                    match[j] = match[j+1] and (p[i] == '.' or p[i] == s[j])
                match[len(s)] = False
            i-=1
            print match
        return match[0]

if __name__ == '__main__':
    print Solution().isMatch("aaa","a*a")
    print Solution().isMatch("abc","a*b*c")