class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSum=0
        minimum=0
        maximum=-float('inf')
        for i in nums:
            prefixSum += i
            maximum=max(maximum, prefixSum - minimum)
            minimum= min(minimum, prefixSum)
        return maximum


        
        