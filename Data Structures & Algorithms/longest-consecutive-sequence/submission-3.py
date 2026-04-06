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
            print(f'ordered[i]: {ordered[i]}')
            if (1 + ordered[i]) in hashset:
                print(f'Found {1+ordered[i]}')
                current +=1
                print(f'Current: {current}')
                i+=1
            else:
                consecutive = max(consecutive, current)
                print(f'Updated: {consecutive}')
                current = 1
                i +=1
        return max(consecutive, current)
