from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        start = 0
        
        for end in range(len(nums)):
            while nums[end] - nums[start] > 1:
                start += 1
            if nums[end] - nums[start] == 1:
                longest = max(longest, end - start + 1)
        
        return longest
