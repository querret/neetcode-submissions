class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]
        length = len(nums)
        final = []

        for i in range(1, length):
            left.append(left[i-1] * nums[i-1])
        for i in range(length - 2, -1, -1):
            right.append(right[-1] * nums[i+1])

        right.reverse()

        for i in range(len(left)):
            final.append(left[i] * right[i])
        
        return final