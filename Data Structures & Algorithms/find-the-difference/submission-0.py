class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmapS = Counter(s)
        hashmapT = Counter(t)
        count = 0

        for i,v in enumerate(t):
            if hashmapS[v] != hashmapT[v]:
                return v 