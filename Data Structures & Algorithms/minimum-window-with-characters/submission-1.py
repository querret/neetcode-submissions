class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = {}, {}
        satisfied = 0
        shortest_string = ""
        length = 0
        left, right = 0, 0

        # get the freqmap of t
        for c in t: 
            if c not in need:
                need[c] = 1
            else: 
                need[c] += 1

        required = len(need)
        
        # sliding window for the substrings
        while right < len(s):
            cur_char = s[right]
            # update the have dict
            if cur_char in need:
                if cur_char not in have:
                    have[cur_char] = 1
                else: 
                    have[cur_char] += 1
            
                # check if the freq number is satisfied
                if have[cur_char] == need[cur_char]:
                    satisfied += 1
            
            # compare the need to have dict
            # update the shortest_string with current window
            # update the wiggly left until shortest
            while satisfied == required:
                # get substring length, compare to shortest_string
                length = right - left + 1
                substr_length = len(shortest_string)
                left_char = s[left]

                if shortest_string == "" or length < len(shortest_string):
                    shortest_string = s[left:right+1]
                if left_char in need:
                    have[left_char] -= 1
                    if have[left_char] < need[left_char]:
                        satisfied -= 1
                left += 1

            # then continue marching right
            right += 1

        # return shortest substring
        return shortest_string