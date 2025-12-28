class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        answer = []
        
        for i in range(n):
            left = sum(nums[0:i])
            right = sum(nums[i+1:n])
            
            answer.append(abs(left - right))
            
        return answer









