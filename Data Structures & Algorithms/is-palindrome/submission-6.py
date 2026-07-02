class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        s1 = s.lower()
        while L <= R:
            if not s1[R].isalnum():
                R-=1
            elif not s1[L].isalnum():
                L+=1
            elif s1[R] == s1[L]:
                L+=1
                R-=1
            else:
                return False
        return True