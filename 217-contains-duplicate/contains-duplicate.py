from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for count in d.values():
            if count > 1:
                return True
          
        return False      
        