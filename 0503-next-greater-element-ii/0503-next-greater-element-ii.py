class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        result=[-1] * len(nums)
        for i in range(2 * len(nums)):
            k= i if i < len(nums) else i % len(nums)
            if not stack and i < len(nums):
                stack.append(k)
            else:
                while stack and nums[stack[-1]] < nums[k]:
                    result[stack[-1]] = nums[k]
                    stack.pop()
                if i < len(nums):
                    stack.append(k)
            
            if not stack and i >= len(nums):
                break
            
        return result 