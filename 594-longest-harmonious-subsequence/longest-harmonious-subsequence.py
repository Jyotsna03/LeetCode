from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        start = 0
        
        for i in range(len(nums)):
            while nums[i] - nums[start] > 1:
                start += 1
            if nums[i] - nums[start] == 1:
                longest = max(longest, i - start + 1)
        
        return longest
