class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = {}, {}
        satisfied = 0
        left, right = 0, 0

        # get the freqmap of t
        for c in t: 
            if c not in need:
                need[c] = 1
            else: 
                need[c] += 1

        required = len(need)
        best_left = 0
        best_length = float("inf")
        
        # sliding window for the substrings
        for right in range(len(s)):
            cur_char = s[right]

            # update the have dict
            if cur_char in need:
                if cur_char not in have:
                    have[cur_char] = 1
                else:
                    have[cur_char] += 1

                # check satisfied/required
                if have[cur_char] == need[cur_char]:
                    satisfied += 1

            # wiggle left forward while valid
            while satisfied == required:
                length = right - left + 1

                # save best length and starting point
                if length < best_length:
                    best_length = length
                    best_left = left

                left_char = s[left]

                if left_char in need:
                    have[left_char] -= 1

                    if have[left_char] < need[left_char]:
                        satisfied -= 1

                left += 1

        # if length is infinity, no substr with matches found
        if best_length == float("inf"):
            return ""

        # slice for final substring
        return s[best_left:best_left + best_length]
