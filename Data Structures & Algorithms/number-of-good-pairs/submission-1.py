class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        count,res = 0,0
        for n,c in hashmap.items():
            res += c * (c - 1) // 2
        return res