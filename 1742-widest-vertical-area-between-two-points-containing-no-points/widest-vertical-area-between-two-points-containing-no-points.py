class Solution(object):
    def maxWidthOfVerticalArea(self,points):
        x_vals = sorted([p[0] for p in points])
        farq = 0
        for i in range(1, len(x_vals)):
            farq = max(farq, x_vals[i] - x_vals[i-1])
        return farq