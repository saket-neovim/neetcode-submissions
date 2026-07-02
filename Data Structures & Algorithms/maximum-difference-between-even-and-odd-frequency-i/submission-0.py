class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        even_list,odd_list = [],[]
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in hashmap:
            if hashmap[i] % 2 == 0:
                even_list.append(hashmap[i])
            else:
                odd_list.append(hashmap[i])
        return max(odd_list) - min(even_list)