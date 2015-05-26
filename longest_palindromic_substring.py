class Solution:
    # @param {string} s
    # @return {string}

    # Manacher Algorithm
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ""
        # save original string using boundary seperated array
        s2 = self.add_boundaries(s)
        # save span length in a array for each char, this is used to check which is the longest
        p = [0] * len(s2)
        # c is the center pos, r is right-most pos, m and n are running positions to compare characters
        c = r = m = n = 0

        for i in range(1, len(s2)):
            # check if current position i is a new start or not
            if i > r:
                p[i] = 0
                m = i-1
                n = i+1
            else:
                i2 = c*2-i
                if p[i2] < r-i:
                    p[i] = p[i2]
                    m = -1
                else:
                    p[i] = r - i
                    n = r + 1
                    m = i*2 - n
            while (m >= 0 and n < len(s2) and s2[m] == s2[n]):
                p[i] += 1
                m -= 1
                n += 1
            if i+p[i] > r:
                c = i
                r = i+p[i]

        l = c = 0
        for i in range(1, len(s2)):
            if l < p[i]:
                l = p[i]
                c = i
        res = s2[c-l:c+l+1]

        return self.remove_boundaries(res)

    def add_boundaries(self, s):
        if s is None or len(s) == 0:
            return ['|','|']
        ss = ['|']
        for i in range(0, len(s)):
            ss.append(s[i])
            ss.append('|')
        return ss

    def remove_boundaries(self, ss):
        if ss is None or len(ss) == 0:
            return []
        ss2 = []
        for i in range(0,(len(ss)-1)/2):
            ss2.append(ss[i*2+1])
        return ''.join(ss2)

if __name__ == '__main__':
    print Solution().add_boundaries('ababapq')
    print Solution().remove_boundaries('|a|b|a|b|a|p|q|')
    print Solution().longestPalindrome('ababapq')
