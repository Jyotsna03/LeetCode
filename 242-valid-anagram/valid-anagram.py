class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sorted          - time O (n log n)
        #return sorted(s) == sorted(t)

        
        if len(s) != len(t): return False
        
        hashMap = {}
        for char in s: 
            hashMap[char] = hashMap.get(char, 0) + 1
        
        for char in t:
            if char not in hashMap or hashMap[char] == 0:
                return False
            else: hashMap[char] -= 1
        
        return True
        