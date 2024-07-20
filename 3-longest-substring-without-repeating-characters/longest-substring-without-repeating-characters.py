class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res    

        #char_index_map = {}
        #maxlen = 0
        #start = -1
        
        #for i, char in enumerate(s):
            #if char in char_index_map and char_index_map[char] > start:
                #start = char_index_map[char]
            #char_index_map[char] = i
            #maxlen = max(maxlen, i - start)
        
        #return maxlen
        