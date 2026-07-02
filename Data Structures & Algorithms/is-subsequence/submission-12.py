class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L,R = 0,0
        i,j = len(s), len(t)
        while L < i and R < j:
            if s[L] == t[R]:
                L+=1
            R+=1
        if L == len(s): return True
        else:
            return False
        
