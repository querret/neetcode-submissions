from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict()
        final = list()

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else: 
                num_count[num] = 1

        ordered = dict(sorted(num_count.items(), key=itemgetter(1), reverse=True))
        list_ordered = list(ordered.keys())

        for i in range(k):
            final.append(list_ordered[i])

        return final