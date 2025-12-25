class Solution(object):
    def buildArray(self, nums):
        a = []
        for i in range(len(nums)):
            a.append(nums[nums[i]])
        return a    


        