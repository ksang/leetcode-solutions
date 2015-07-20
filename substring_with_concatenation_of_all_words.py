class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if len(words) < 1 or len(s) == 0:
            return []
        wdict = {}
        for w in words:
            if wdict.has_key(w):
                wdict[w] += 1
            else: wdict[w] = 1
        res = []
        size = len(words[0])
        i = 0
        # starting posistion has 0 - size-1 possibilies
        for i in range(0,size):
            j = left = i
            count = 0 # counter for word match
            tdict = {}
            while j <= len(s)-size:
                key = s[j:j+size]
                if wdict.has_key(key):
                    if tdict.has_key(key):
                        tdict[key] += 1
                    else: tdict[key] = 1
                    if tdict[key] <= wdict[key]:
                        count += 1
                    else:
                        # more word than in the word dict, move substring from left
                        while tdict[key] > wdict[key]:
                            ss = s[left:left+size]
                            tdict[ss] -= 1
                            if tdict[ss] < wdict[ss]: count -= 1
                            left += size
                    if count == len(words):
                        res.append(left)
                        tdict[s[left:left+size]] -= 1
                        count -= 1
                        left += size
                else:
                    # not a valid word, reset vars, move left to current pos
                    tdict.clear()
                    count = 0
                    left = j+size
                j += size

        return res

if __name__ == '__main__':
    print Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])