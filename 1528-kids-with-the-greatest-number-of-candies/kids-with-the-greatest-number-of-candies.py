class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for i in candies:
            if i+extraCandies >=max(candies):
                result.append(True)
            else:
                result.append(False)    
        return result