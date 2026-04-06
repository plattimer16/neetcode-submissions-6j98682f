class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)
        ordered = sorted(list(set(nums)))
        print(ordered)
        i = 0
        length = len(ordered)
        consecutive = 1
        current = 1
        while i < length:
            if (1 + ordered[i]) in hashset:
                current +=1
                i+=1
            else:
                consecutive = max(consecutive, current)
                current = 1
                i +=1
        return max(consecutive, current)
