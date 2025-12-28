class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):
            a = 0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    a += 1
            result.append(a)
        return result           
