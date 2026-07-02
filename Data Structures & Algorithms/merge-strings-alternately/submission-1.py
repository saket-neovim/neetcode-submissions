class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = min(len(word1), len(word2))
        newString = ""
        while l < r:
            newString += word1[l]
            newString += word2[l]
            l+=1
            if l >= r:
               newString += word1[l::] 
               newString += word2[l::] 
        return newString