class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        max = 0
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
            if hashmap[num] > len(nums) / 2:
                return num