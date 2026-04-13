class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = Counter(t)
        found_letters = Counter()
        have = 0
        need = len(t_letters)
        l, r = 0, 0
        min_l, min_r = 0, 0
        min_window = 1001
        for r in range(len(s)):
            #print(f'Window : {s[l:r + 1]}')
            if s[r] in t_letters:
                found_letters[s[r]] = 1 + found_letters.get(s[r], 0)
                if found_letters[s[r]] == t_letters[s[r]]:
                    have += 1
                    #print(f'Have {have} need {need}')
            while have == need:
                #print('have == need')
                #print(f'Current Window: {l} {r}')
                if (r - l + 1) <min_window:
                    min_window = r - l + 1
                    min_l, min_r = l, r
                    #print(f'Found min window: {min_window}')
                if s[l] in found_letters:
                    found_letters[s[l]] -= 1
                if found_letters[s[l]] < t_letters[s[l]]:
                    have -= 1
                l += 1
        if min_window > 1000:
            return ""
        return s[min_l: min_r+1]
            
        


            
            
            