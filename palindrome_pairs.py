class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wd = {}
        res = []
        for i,w in enumerate(words):
        	wd[w] = i
        for w in words: