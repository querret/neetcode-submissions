class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for num in nums:
        #     if target-num in nums:
        #         return [nums.index(num), nums.index(target-num, nums.index(num))]

#  use a hashmap to store seen. if complement is in the seen hashmap, that's the valid pair.

        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen.get(target-nums[i]), i]
            seen[nums[i]] = i