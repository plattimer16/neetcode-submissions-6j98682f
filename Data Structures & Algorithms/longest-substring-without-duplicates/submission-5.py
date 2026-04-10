class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        seen = set(s[0])
        res = 1
        cur = 1
        while r < len(s):
            print(l, r, seen)
            
            if s[r] not in seen:
                print('new char ' + s[r])
                seen.add(s[r])
                cur += 1
                if cur > res:
                    res = cur
                r += 1
            
            else:
                print('dupe ' + s[r])
                while s[l] != s[r]:
                    seen.remove(s[l])
                    cur -= 1
                    l +=1
                print(seen)
                l += 1
                r += 1
        return res


        