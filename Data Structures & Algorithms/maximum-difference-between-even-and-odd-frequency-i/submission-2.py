class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        evenList,oddList = [],[]
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in hashmap:
            if hashmap[i] % 2 == 0:
                evenList.append(hashmap[i])
            else:
                oddList.append(hashmap[i])
        return max(oddList) - min(evenList)