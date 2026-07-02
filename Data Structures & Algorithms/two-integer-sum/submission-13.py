class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums2 = []
        for i,v in enumerate(nums):
            nums2.append([v, i])
        
        nums2.sort()

        i,j = 0, len(nums) - 1

        while i < j:
            current = nums2[i][0] + nums2[j][0]
            if current > target:
                j-=1
            elif current < target:
                i+=1
            else:
                return [min(nums2[i][1],nums2[j][1]),max(nums2[i][1],nums2[j][1])]
