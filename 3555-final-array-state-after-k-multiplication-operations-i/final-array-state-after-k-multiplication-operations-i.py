class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            a = min(nums)
            index = nums.index(a)
            nums[index] = a*multiplier
        return nums

                

        