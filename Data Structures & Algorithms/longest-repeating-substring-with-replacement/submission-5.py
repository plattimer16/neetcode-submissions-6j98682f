class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        letters = Counter()
        l = 0
        res = 0
        for r in range(len(s)):
            letters[s[r]] += 1
            window_size = (r - l + 1)
            most_common = letters.most_common(1)[0]
            if window_size - most_common[1] <= k:
                res = max(window_size, res)
            else:
                letters[s[l]] -= 1
                l += 1
        return res

            