class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        count = 0
        
        for num in nums:
            count += freq[num - k]
            count += freq[num + k]
            freq[num] += 1
            
        return count