class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        s2rev = ""
        for i in s:
            if i.isalnum():
                s2 += i.lower()
        for i in range(len(s2) -1 ,-1, -1):
            s2rev += s2[i].lower()
        if s2 == s2rev:
            return True
        else:
            return False

