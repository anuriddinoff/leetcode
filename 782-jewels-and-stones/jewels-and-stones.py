class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        result = 0
        for i in jewels:
            for j in stones:
                if i==j:
                    result+=1
        return result            
        