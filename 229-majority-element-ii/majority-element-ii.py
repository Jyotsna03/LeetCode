class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        result = []
        for i in set(nums):
            if nums.count(i) > n:
                result.append(i)
        return result
            
        