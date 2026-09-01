class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        right = 0
        substring = set()

        while right < len(s):
            if s[right] in substring:
                substring.remove(s[left])
                left += 1
                continue

            substring.add(s[right])
            right += 1

            if len(substring) > max_length:
                    max_length = len(substring)
        return max_length
