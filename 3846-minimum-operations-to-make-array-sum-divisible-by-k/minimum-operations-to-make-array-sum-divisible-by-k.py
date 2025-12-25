class Solution(object):
    def minOperations(self, nums, k):
        total = sum(nums)
        remainder = total % k
        return remainder