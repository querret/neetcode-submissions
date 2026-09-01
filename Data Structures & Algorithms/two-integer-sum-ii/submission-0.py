class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers)-1
        sum = numbers[i1] + numbers[i2]

        while sum != target:
            if sum > target:
                i2 -= 1
            if sum < target:
                i1 += 1

            sum = numbers[i1] + numbers[i2]
        
        return [i1+1,i2+1]
