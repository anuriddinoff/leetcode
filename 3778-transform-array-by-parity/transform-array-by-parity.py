class Solution(object):
    def transformArray(self, nums):
        a = [0 if num % 2 == 0 else 1 for num in nums]
        a.sort()
        return a