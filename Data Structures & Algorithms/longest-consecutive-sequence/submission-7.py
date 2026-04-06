class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_consecutive = 1
        if not nums:
            return 0
        for num in hashset:
            current = 1
            # Check if root, only run loop on roots. Results in O(N)
            if (num - 1) not in hashset:
                i = 1
                while (num + i) in hashset:
                    current +=1
                    i+=1
                longest_consecutive = max(longest_consecutive, current)
        return longest_consecutive
