class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        i = 0
        length = len(nums)
        while i < (length - 1):
            if nums[i] > 0:
                break
            first = i + 1
            last = length - 1
            while first < last:
                if nums[first] + nums[last] == -nums[i]:
                    triplet = (nums[i], nums[first], nums[last])
                    triplets.add(triplet)
                    first+=1
                    last-=1
                elif nums[first] + nums[last] > -nums[i]:
                    last -=1
                else:
                    first+=1
            i+=1
        return list(triplets)
                