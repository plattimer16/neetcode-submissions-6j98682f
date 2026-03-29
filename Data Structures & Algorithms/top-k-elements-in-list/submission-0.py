class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        ans = []
        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
        sorted_dict = {k : v for k, v in sorted(num_count.items(), key=lambda item: item[1], reverse=True)}
        x = k
        for key in sorted_dict.keys():
            if x:
                ans.append(key)
                x-=1
            else:
                break
        return ans
