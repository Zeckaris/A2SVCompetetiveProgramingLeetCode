class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        firstArrayPointer=m - 1
        secondArrayPointer= n - 1
        mergedPointer= m + n - 1
        while firstArrayPointer >= 0 and secondArrayPointer >= 0:
            if nums1[firstArrayPointer] > nums2[secondArrayPointer]:
                nums1[mergedPointer] = nums1[firstArrayPointer]
                firstArrayPointer -= 1
            else:
                nums1[mergedPointer] = nums2[secondArrayPointer]
                secondArrayPointer -= 1
            mergedPointer -= 1

        while secondArrayPointer >= 0:
            nums1[mergedPointer] = nums2[secondArrayPointer]
            secondArrayPointer -= 1
            mergedPointer -= 1
        