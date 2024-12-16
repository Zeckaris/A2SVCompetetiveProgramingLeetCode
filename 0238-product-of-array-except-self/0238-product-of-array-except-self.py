class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct=[1]
        suffixProduct=[1]
        product=1
        answer=[]
        for i in nums:
            product *= i
            prefixProduct.append(product)
        
        product=1
        for i in range(len(nums) - 1,-1,-1):
            product *= nums[i]
            suffixProduct.append(product)
            
        
        for i in range(len(nums)):
            res= prefixProduct[i] * (suffixProduct[len(nums) - (i + 1)])
            answer.append(res)
        
        return answer



        