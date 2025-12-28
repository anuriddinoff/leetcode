class Solution(object):
    def countNegatives(self, grid):
        result = 0
        for i in grid:
            for j in i:
                if j<0:
                    result+=1
        return result            
        