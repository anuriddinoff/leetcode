class Solution(object):
    def minElement(self, nums):
        result = []
        for i in nums:
            a = 0
            for j in str(i):
                a +=int(j)
            result.append(a)
        return min(result)        