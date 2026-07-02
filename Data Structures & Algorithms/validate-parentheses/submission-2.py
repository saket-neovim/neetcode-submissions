class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(","]":"[","}":"{"}
        stack = []
        for c in s:
            if c in hashmap:
                if len(stack) != 0 and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        return True