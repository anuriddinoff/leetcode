class Solution(object):
    def findClosest(self, x, y, z):
        a = abs(x - z)
        b = abs(y - z)
        return 1 if a < b else 2 if a > b else 0