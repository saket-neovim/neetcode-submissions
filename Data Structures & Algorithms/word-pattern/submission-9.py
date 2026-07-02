class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapPS, mapSP = {}, {}
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        for char, word in zip(pattern, words):
            if char not in mapPS and word not in mapSP:
                mapPS[char] = word
                mapSP[word] = char
            else:
                if mapPS.get(char) != word and mapSP.get(word) != char:
                    return False
        return True
