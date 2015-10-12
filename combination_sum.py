CAND = [2,3,6,7]

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def sumrun(self, cand, target):
        res = []
        for idx, c in enumerate(cand):
            if c == target:
                res += [[c]]
            elif target > c:
                # in the next loop, remain the element ifself so includes unlimited count.
                res += [[c]+x for x in self.sumrun(cand[idx:], target-c)]
            else:
                break
        return res

    def combinationSum(self, candidates, target):
        return self.sumrun(sorted(candidates), target)

if __name__ == '__main__':
    print Solution().combinationSum(CAND,7)