class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        n = len(s)
        count = 0
        
        left = 0
        right = n - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                l, r = left, right
                while r > l and s[r] != s[left]:
                    r -= 1
                
                if r == l:
                    s[l], s[l + 1] = s[l + 1], s[l]
                    count += 1
                else:
                    while r < right:
                        s[r], s[r + 1] = s[r + 1], s[r]
                        r += 1
                        count += 1
                    left += 1
                    right -= 1
        
        return count


