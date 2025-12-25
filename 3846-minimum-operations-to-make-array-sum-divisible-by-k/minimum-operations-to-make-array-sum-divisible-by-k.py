class Solution(object):
    def minOperations(self, nums, k):
        result = 0
        for i in nums:
            result += i
        final_result = result % k
        return final_result 
        
           
        