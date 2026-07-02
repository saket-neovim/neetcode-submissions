class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        t2 = sorted(t)

        return s1 == t2

        