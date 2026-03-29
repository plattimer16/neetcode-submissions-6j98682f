class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for word in strs:
            length = len(word)
            if length < 10:
                length = '00' + str(length)
            elif length < 100:
                length = '0' + str(length)
            string = str(length) + '#' + word
            coded = coded + string
        return coded

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        decoded = []
        while i < len(s):
            total_chars = int(s[i:i+3])
            i = i + 4
            chars = []
            for j in range(total_chars):
                chars.append(s[i+j])
            chars = "".join(chars)
            decoded.append(chars)
            i = i + total_chars

        return decoded