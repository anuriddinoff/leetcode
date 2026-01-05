class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = sum(int(d) for num in nums for d in str(num))
        return abs(element_sum - digit_sum)