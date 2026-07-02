class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l, space = 0," "               
        for i in range(len(s) - 1,-1,-1):
            if s[i] != space:
                l+=1
            elif s[i] == space and l > 0:
                return l
        return l