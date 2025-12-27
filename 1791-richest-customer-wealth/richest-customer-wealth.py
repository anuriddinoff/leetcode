class Solution(object):
    def maximumWealth(self, accounts):
        result = 0
        for i in accounts:
            a = sum(i)
            if a>=result:
                result = a
        return result      

        