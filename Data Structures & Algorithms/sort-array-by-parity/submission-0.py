class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L = 0
        temp = 0
        for R in range(len(nums)):
            if nums[R] % 2 == 0:
                temp = nums[R]
                nums[R] = nums[L]
                nums[L] = temp
                L+=1
        return nums