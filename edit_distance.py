class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = range(len(word2)+1)
        for i in xrange(len(word1)):
        	dist_ij = i
        	dist[0] = i+1
        	for j in xrange(len(word2)):
        		if word1[i] == word2[j]:
        			dist[j+1] = dist_ij
        			dist_ij = dist[j+1]
        		else:
        			dist[j+1] = min(dist[j], dist_ij, dist[j+1]) + 1

        			72/115