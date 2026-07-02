class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()

        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
            else:
                hashset.remove(nums[i])
        return list(hashset)[0]