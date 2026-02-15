class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(int(num[i]) for i in range(0, len(num), 2)) == \
               sum(int(num[i]) for i in range(1, len(num), 2))