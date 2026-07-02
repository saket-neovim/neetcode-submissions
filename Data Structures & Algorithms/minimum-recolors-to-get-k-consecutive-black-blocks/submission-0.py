class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L = 0
        countW = 0
        minC = k
        for R in range(len(blocks)):
            if blocks[R] == "W":
                countW+=1
            if R - L + 1 == k:
                minC = min(minC, countW)
                if blocks[L] == "W":
                    countW -= 1
                L+=1
        return minC
    