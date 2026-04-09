class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1
        current_substring = {s[0]: 0}
        i = 1
        while i < len(s):
            #print(i)
            if s[i] in current_substring:
                print(s[i], current_substring)
                longest = max(longest, len(current_substring))
                i = current_substring.get(s[i]) + 1
                current_substring.clear()
                #current_substring[s[i]] = i
            else:
                current_substring[s[i]] = i
                i += 1
        longest = max(longest, len(current_substring))
        return longest
        