class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = Counter(s)
        hashmapT = Counter(t)

        if len(s) != len(t):
            return False
        
        for i,v in enumerate(s):
            if hashmapS[v] != hashmapT[v]:
                return False
        return True