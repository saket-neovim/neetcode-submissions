class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        count = 0
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            elif num in hashmap:
                hashmap[num] += 1
        for i in hashmap:
            if hashmap[i] == 1:
                pass
            else:
                count += 1
        if count > 0:
            return True
        else:
            return False                       