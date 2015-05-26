class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        d = {}
        i = res = count = 0
        cur_str = [0,0]
        while i < len(s):
            if d.has_key(s[i]):
                res = max(res, cur_str[1]-cur_str[0])
                if d[s[i]] >= cur_str[0]:
                    cur_str[0] = d[s[i]] + 1

            d[s[i]] = i
            i += 1
            cur_str[1] = i
        return max(res, cur_str[1]-cur_str[0])

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abba")
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("dvdfxa")