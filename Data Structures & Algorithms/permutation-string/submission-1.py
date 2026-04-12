class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = Counter(s1)
        window_letters = collections.defaultdict(int)
        len1, len2 = len(s1), len(s2)
        for r in range(len(s2)):
            print(r)
            window_letters[s2[r]] += 1
            if r >= len1:
                if window_letters[s2[r - len1]] == 1:
                    window_letters.pop(s2[r-len1])
                else:
                    window_letters[s2[r - len1]] -= 1
            if window_letters == letters:
                return True

        return False

