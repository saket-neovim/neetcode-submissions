class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for num in nums:
            if hashmap[num] % 2 != 0:
                return False
        return True
                
            