class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        return sum(
            num for i, num in enumerate(nums) 
            if bin(i).count('1') == k
        )
        