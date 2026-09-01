class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current = 0
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num-1 not in nums_set:
                current = 1
                next_num = num + 1

                while next_num in nums_set:
                    current += 1
                    next_num += 1

                if current > longest:
                    longest = current

        return longest