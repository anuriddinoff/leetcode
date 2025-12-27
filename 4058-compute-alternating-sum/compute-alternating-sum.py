class Solution(object):
    def alternatingSum(self, nums):
        result = 0
        for i in range(len(nums)):
            if i%2 ==0:
                result +=nums[i]
            else:
                result-=nums[i]
        return result            
        