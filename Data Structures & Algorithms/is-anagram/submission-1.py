class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        for letter in t:
            if letter not in hashmap or hashmap[letter] <= 0:
                return False
            else:
                hashmap[letter] -= 1
        return True