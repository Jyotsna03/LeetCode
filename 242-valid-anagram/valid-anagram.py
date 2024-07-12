class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sorted          - time O (n log n)
        return sorted(s) == sorted(t)
        