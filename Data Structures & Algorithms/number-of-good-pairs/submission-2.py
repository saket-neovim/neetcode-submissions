class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                res += hashmap[num]
                hashmap[num] += 1
        return res
