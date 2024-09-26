class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]
        output = " ".join(words)
        return output 