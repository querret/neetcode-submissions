class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_char = {}
        t_char = {}

        for c in s:
            if c not in s_char:
                s_char[c] = 0
            s_char[c] += 1

        for c in t:
            if c not in t_char:
                t_char[c] = 0
            t_char[c] += 1

        if s_char == t_char:
            return True
        return False
        # return sorted(s) == sorted(t)
        
        