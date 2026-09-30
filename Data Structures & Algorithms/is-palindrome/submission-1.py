class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        inv_s = ""
        for i in reversed(cleaned):
            inv_s += i
        
        return cleaned == cleaned[::-1]
