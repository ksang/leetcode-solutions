class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if len(words) < 1 or len(s) == 0:
            return []
        wdict = {}
        for idx,w in enumerate(words):
            if wdict.has_key(w):
                wdict[w] += 1
            else: wdict[w] = 1
        print wdict
        res = []
        size = len(words[0])
        i = 0
        while i <= len(s)-size*len(words):
            rflag = True
            tdict = wdict.copy()
            j = i
            while j < i+size*len(words):
                key = s[j:j+size]
                if tdict.has_key(key):
                    if tdict[key] >= 1:
                        tdict[key] -= 1
                        j += size
                    else:
                        i += 1
                        rflag = False
                        break
                else:
                    i += 1
                    rflag = False
                    break
            if rflag == True:
                for item in tdict.values():
                    if item != 0:
                        rflag = False
                        i += 1
                        break
            if rflag == True:
                res.append(i)
                i += 1

        return res

if __name__ == '__main__':
    print Solution().findSubstring("abaababbaba", ["ab","ba","ab","ba"])