class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = Counter(s)
        hashmap2 = Counter(t)
        if len(s) != len(t):
            return False
        if hashmap1 == hashmap2:
            return True
        return False