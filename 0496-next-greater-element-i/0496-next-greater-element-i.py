class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hsh=dict()
        for i in range(len(nums1)):
            hsh[nums1[i]]= i
        
        stack=[]
        result=[-1] * len(nums1)
        for j in nums2:
            if stack != []:
                while j >  stack[-1]:
                    index= hsh[stack[-1]]
                    result[index]= j
                    stack.pop()
                    if stack == []:
                        break
                if j in hsh:
                    stack.append(j)
            else:
                if j in hsh:
                    stack.append(j)
                
        
        return result