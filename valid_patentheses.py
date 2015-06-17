import sys
class Solution:
    # @param {string} s
    # @return {boolean}
    pmap = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    def isValid(self, s):
        todo = ""
        for c in s:
            if c in self.pmap.keys():
                if len(todo) == 0:
                    return False
                if todo[-1] == self.pmap[c]:
                    todo = todo[:-1]                    
                else:
                    return False
            else:
                todo += c
        if len(todo) == 0: return True
        else: return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please provide parentheses pattern"
        sys.exit(0)
    print Solution().isValid(sys.argv[1])
