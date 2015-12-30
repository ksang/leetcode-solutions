import sys

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = cow = 0
        rest = ""
        secret_dict = {}
        for i,s in enumerate(secret):
            if s == guess[i]:
                bull += 1
            else:
                rest += guess[i]
                if secret_dict.has_key(s):
                    secret_dict[s] += 1
                else:
                    secret_dict[s] = 1                
        for g in rest:
            if secret_dict.has_key(g):
                if secret_dict[g] > 0:
                    secret_dict[g] -= 1
                    cow += 1
        return "%sA%sB" % (bull, cow)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print Solution().getHint(sys.argv[1], sys.argv[2])
    else: print "Please input secret and guess"
