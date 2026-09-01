class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""

        for c in s:
            if c.isalnum():
                cleaned_s += c.lower()

        half_length = len(cleaned_s) // 2

        for i in range(half_length):
            if cleaned_s[i] != cleaned_s[-1-i]:
                return False
        return True