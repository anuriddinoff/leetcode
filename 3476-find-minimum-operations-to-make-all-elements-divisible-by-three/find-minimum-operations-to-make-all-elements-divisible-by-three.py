class Solution(object):
    def minimumOperations(self, nums):
        result = 0
        for i in range(len(nums)):
            if nums[i]!= 3:
                a = min(nums[i]%3, 3-(nums[i]%3))
                result+=a
        return result        



