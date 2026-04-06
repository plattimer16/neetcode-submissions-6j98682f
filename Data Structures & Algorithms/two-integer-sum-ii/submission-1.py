class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1
        while first < second:
            summation = (numbers[first] + numbers[second])
            if  summation == target:
                return [first + 1, second + 1]
            elif summation > target:
                second -=1
            else:
                first +=1
        return []