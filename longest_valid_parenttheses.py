import sys

class Solution:
    # @param {string} s
    # @return {integer}

    # stack solution
    def lvp(self,s):
        stack = []
        ret = 0
        # last is used to record last end of pattern section
        last = -1
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                    if len(stack) > 0:
                        # there are pending ( in the stack, which means current section should start from there
                        r = i-stack[-1]
                    else: # nothing in the stack, lengh start from current section
                        r = i-last
                    ret = max(ret,r)
                else:
                    last = i
        return ret

    # dp solution
    def longestValidParentheses(self, s):
        if len(s) == 0: return 0
        stack = []
        # r is the result array 
        r = [0]*len(s)
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    # get the starting index j
                    j = stack.pop()
                    r[i] = i-j+1
                    if j > 0:
                        # combine length of two sections
                        r[i] += r[j-1]
        return max(r)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please provide parentheses pattern"
        sys.exit(0)
    print Solution().lvp(sys.argv[1])
    print Solution().longestValidParentheses(sys.argv[1])