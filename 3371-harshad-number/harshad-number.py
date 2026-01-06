class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n=x
        digit_sum = 0

        while n > 0:
            digit_sum += n % 10
            n //= 10

        return digit_sum if x % digit_sum == 0 else -1