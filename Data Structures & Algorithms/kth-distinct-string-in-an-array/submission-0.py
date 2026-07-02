class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = Counter(arr)
        res = []
        for e in arr:
            if hashmap[e] == 1:
                res.append(e)
        if k > len(res):
            return ""
        return res[k - 1]
