class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort characters in string into alphabet
        # if that tuple key exists in seen, append whole word to list at that key in the dict

        # format the result dict and output the dict
        # final = []
        grouped = dict()

        for word in strs:
            ordered = "".join(sorted(word))
            if ordered in grouped:
                grouped[ordered].append(word)
            else: 
                grouped[ordered] = [word]

        return list(grouped.values())
            