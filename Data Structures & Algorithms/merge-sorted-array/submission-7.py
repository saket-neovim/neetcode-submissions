class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = m - 1
        end2 = n - 1
        end = len(nums1) - 1

        while start >= 0 and end2 >= 0:
            if nums1[start] > nums2[end2]:
                nums1[end] = nums1[start]
                start -= 1
                end -=1
            else:
                nums1[end] = nums2[end2]
                end2-=1
                end-=1
        while end2 >= 0:
            nums1[end] = nums2[end2]
            end -= 1
            end2 -= 1

