class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,v in enumerate(nums):
            complement = target - v
            if complement in hashmap and hashmap[complement] != i:
                return [hashmap[complement],i]
            hashmap[v] = i
        return []