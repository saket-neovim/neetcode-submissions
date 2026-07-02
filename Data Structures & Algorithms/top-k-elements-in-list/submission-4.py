class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        arr = []
        for num,freq in hashmap.items():
            arr.append([freq,num])
        arr.sort()
        res = []
        for i in range(len(arr) - 1, len(arr) - 1 - k, - 1):
            res.append(arr[i][1])
        return res