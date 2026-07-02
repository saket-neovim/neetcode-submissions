class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = 0
        res = [0] * len(nums)
        R = len(nums) - 1 
        P = len(nums) - 1
        while L <= R:
            if abs(nums[R]) < abs(nums[L]):
                res[P] = nums[L] * nums[L]
                L+=1
            else:
                res[P] = nums[R] * nums[R]
                R-=1
            P-=1
        return res