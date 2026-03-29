class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for letter in s:
            hashmap[letter] = 1 + hashmap.get(letter, 0)
        for letter in t:
            if hashmap.get(letter, 0) <= 0:
                return False
            else:
                hashmap[letter] -= 1
        return True
