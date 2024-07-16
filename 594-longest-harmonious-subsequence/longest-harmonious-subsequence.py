from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        res = 0
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                count = nums.count(nums[i]) + nums.count(nums[i + 1])
                res = max(res, count)
        
        return res

