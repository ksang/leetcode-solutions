class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for s in strs[1:]:
            if len(s) < len(prefix):
                prefix = prefix[0:len(s)]
            for idx,c in enumerate(s):
                if idx > len(prefix)-1:
                    break
                if prefix[idx] != c:
                    prefix = prefix[0:idx]
                    break
            if prefix == '': break
        return prefix

if __name__ == '__main__':
    data = ['abcd','abc']
    print Solution().longestCommonPrefix(data)

