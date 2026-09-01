
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        
        for word in strs:
            anagram_id = [0] * 26
            for c in word:
                anagram_id[ord(c) - ord('a')] += 1
            key = tuple(anagram_id)
            final.setdefault(key, []).append(word)

        return list(final.values())