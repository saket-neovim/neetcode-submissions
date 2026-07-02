class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1), len(word2)
        i,j = 0,0
        final = []
        while i < m and j < n:
            final.append(word1[i])
            final.append(word2[j])
            i+=1
            j+=1
        final.append(word1[i:])
        final.append(word2[j:])
        return "".join(final)