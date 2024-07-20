class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        maxlen = 0
        start = -1
        
        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] > start:
                start = char_index_map[char]
            char_index_map[char] = i
            maxlen = max(maxlen, i - start)
        
        return maxlen
        