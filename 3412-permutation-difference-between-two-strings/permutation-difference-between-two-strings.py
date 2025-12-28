class Solution(object):
    def findPermutationDifference(self, s, t):
        n= len(s)
        result = 0
        for i in range(n):
            for j in range(n):
                if s[i]==t[j]:
                    result+=abs(i-j)
        return result            