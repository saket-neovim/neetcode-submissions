class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t= "".join(sorted(t))
        count = 0
        for i in range(len(sorted_s)):
            if sorted_s[i -1] == sorted_t[i -1]:
                count+=1
        if count == len(sorted_s) and count == len(sorted_t):
            return True
        return False