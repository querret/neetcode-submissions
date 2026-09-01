class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for index, num in enumerate(nums):
            remainder = target - num

            if remainder in seen:
                return [seen[remainder], index]
            seen[num] = index