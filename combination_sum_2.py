CAND = [10,1,2,7,6,1,5]

class Solution(object):

    def sumrun2(self, cands, target):
        res = []
        for idx,c in enumerate(cands):
            if idx > 0:
                if c == cands[idx-1]:
                    continue
            if target == c:
                res += [[c]]
            elif target > c:
                res += [[c]+x for x in self.sumrun2(cands[idx+1:],target-c)]
            else:
                break
        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.sumrun2(sorted(candidates), target)
        
if __name__ == '__main__':
    print Solution().combinationSum2(CAND,8)