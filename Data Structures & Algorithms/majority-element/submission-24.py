class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for i,v in enumerate(nums):
            if hashmap[v] > len(nums)/2:
                return v