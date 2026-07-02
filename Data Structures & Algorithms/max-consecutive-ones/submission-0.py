class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxC = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
                maxC = max(count, maxC)
            else:
                count = 0
        return maxC