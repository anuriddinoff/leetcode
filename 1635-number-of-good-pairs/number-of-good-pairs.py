class Solution(object):
    def numIdenticalPairs(self, nums):
        a= 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j:
                    a+=1
        return a            

        