class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        arr = []
        for num,freq in hashmap.items():
            arr.append([freq,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res