class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        X = set(nums1)
        Y = set(nums2)
        return X & Y
        