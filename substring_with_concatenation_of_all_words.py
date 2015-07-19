class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if len(words) < 1 or len(s) == 0:
            return []
        key = words[0]
        res = []
        size = len(key)
        i = pos = 0
        while pos >= 0:
            pos = s[i:].find(key)
            right = pos+i+size
            left = pos+i-size
            tl = []
            while right <= len(s)-size:
                temp = s[right:right+size]
                if temp in words[1:] and temp not in tl:
                    tl.append(temp)
                else: break
                right += size
            while left >= 0:
                temp = s[left:left+size]
                if temp in words[1:] and temp not in tl:
                    tl.append(temp)
                else: break
                left -= size
            if len(tl) == len(words)-1:
                res.append(left+size)  
            right = pos+i+size
            left = pos+i-size
            tl = []
            while left >= 0:
                temp = s[left:left+size]
                if temp in words[1:] and temp not in tl:
                    tl.append(temp)
                else: break
                left -= size
            while right <= len(s)-size:
                temp = s[right:right+size]
                if temp in words[1:] and temp not in tl:
                    tl.append(temp)
                else: break
                right += size
            if len(tl) == len(words)-1:
                if res[-1] != left+size:
                    res.append(left+size)  
            # move to the next find
            i = i+pos+size
        return res

if __name__ == '__main__':
    print Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])