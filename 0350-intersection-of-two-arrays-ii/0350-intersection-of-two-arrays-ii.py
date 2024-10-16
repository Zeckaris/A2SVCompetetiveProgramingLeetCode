class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hsmp=dict()
        intersection=[]
        selected= nums1 if len(nums1) < len(nums2) else nums2
        for i in  selected:
            if i not in hsmp:
                hsmp[i] = 1
            else:
                hsmp[i] += 1
        check= nums1 if nums1 != selected else nums2
        for i in check:
            if i in hsmp:
                hsmp[i] -= 1
                intersection.append(i)
                if hsmp[i] == 0:
                    hsmp.pop(i)
        return intersection
            
        