class Solution(object):
    def mirrorDistance(self, n):
        a = str(n)
        return abs(int(a[::-1])-n)
        