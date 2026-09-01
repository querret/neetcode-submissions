class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = set(list())
        sorted_nums = sorted(nums)

        for i, num in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            left = i + 1
            right = len(sorted_nums)-1

            while left < right:
                current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if current_sum == 0:
                    final.add(tuple([sorted_nums[i], sorted_nums[left], sorted_nums[right]]))
                    left += 1
                    right -= 1
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                
        return list(final)
