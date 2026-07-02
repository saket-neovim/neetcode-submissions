class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = Counter(s)
        evenCount,oddCount = [],[]
        for i in hashmap:
            if hashmap[i] % 2 == 0:
                evenCount.append(hashmap[i])
            else:
                oddCount.append(hashmap[i])
        return max(oddCount) - min(evenCount)