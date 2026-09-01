class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = self.hash_count(s)
        t_count = self.hash_count(t)

        if s_count == t_count:
            return True
        return False
            
    def hash_count(self, word):
        count = dict()
        for c in word:
            if c in count:
                count[c] += 1
            else: count[c] = 1
        return count