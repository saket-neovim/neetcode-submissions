class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            elif num in seen:
                seen.remove(num)
        return list(seen)[0]