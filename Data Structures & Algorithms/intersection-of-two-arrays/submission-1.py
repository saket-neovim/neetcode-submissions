class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        res = []
        for num in nums1:
            hashmap[num] = 1
        for num in nums2:
            if hashmap[num] == 1:
                hashmap[num] = 0
                res.append(num)
        return res