class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict()
        max_freq = len(nums)
        freq_map = dict()
        final = []

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else: 
                num_count[num] = 1

        for num, freq in num_count.items():
            if freq in freq_map:
                freq_map[freq].append(num)
            else:
                freq_map[freq] = [num]
        
        for freq in range(max_freq, 0, -1):
            if freq in freq_map:
                final.extend(freq_map[freq])

                if len(final) >= k:
                    return final[:k]