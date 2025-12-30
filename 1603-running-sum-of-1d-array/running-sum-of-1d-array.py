class Solution(object):
    def runningSum(self, nums):
        new = []
        for i in range(len(nums)):
            a = sum(nums[:i+1])
            new.append(a)
        return new
        