class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charToWord = {}
        wordToChar = {}
        words = s.split()
        wordC, patternC = 0,0
        for word in words:
            wordC += 1
        for c in pattern:
            patternC += 1
        if wordC != patternC:
            return False
        for i in range(len(pattern)):
            if pattern[i] not in charToWord and words[i] not in wordToChar:
                charToWord[pattern[i]] = words[i]
                wordToChar[words[i]] = pattern[i]
            else:
                if charToWord.get(pattern[i]) != words[i] or wordToChar.get(words[i]) != pattern[i]:
                    return False
        return True
