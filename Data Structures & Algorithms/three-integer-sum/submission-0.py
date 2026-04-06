class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        sorted_nums = sorted(nums)
        print(sorted_nums)
        i = 0
        length = len(sorted_nums)
        while i < (length - 1):
            first = i + 1
            last = length - 1
            while first < last:
                if sorted_nums[first] + sorted_nums[last] == -sorted_nums[i]:
                    triplet = (sorted_nums[i], sorted_nums[first], sorted_nums[last])
                    if triplet not in triplets:
                        triplets.add(triplet)
                    print(i, first, last)
                    first+=1
                    last-=1
                elif sorted_nums[first] + sorted_nums[last] > -sorted_nums[i]:
                    last -=1
                else:
                    first+=1
            i+=1
        return list(triplets)
                