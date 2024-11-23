class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        maxSum= s
        for  i in range(k,len(nums)):
            s = s - nums[i - k] + nums[i]
            maxSum= maxSum if  maxSum >= s else s
        avg= maxSum / k
        return avg

            
            

