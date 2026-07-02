class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        while L < R:
            if s[R] == s[L]:
                L+=1
                R-=1
            else:
                skipl = s[L + 1:R + 1]
                skipr = s[L : R]
                if skipl != skipl[::-1] and skipr != skipr[::-1]:
                    return False
                L+=1
                R-=1
        return True