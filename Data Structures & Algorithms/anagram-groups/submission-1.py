class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [[strs[0]]] # start with first
        i = 1
        while i < len(strs):
            added = False
            letters = Counter(strs[i])
            for anagram in anagrams:
                if letters == Counter(anagram[0]):
                    anagram.append(strs[i])
                    added = True
            if not added:
                anagrams.append([strs[i]])
            i+=1
        return anagrams

