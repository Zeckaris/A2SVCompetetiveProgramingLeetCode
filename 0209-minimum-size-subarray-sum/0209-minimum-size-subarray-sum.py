class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #dynamic sliding window
        begin= 0
        end= 0
        sumation = 0
        minLength= float('inf')
        flag= False
        while end < len(nums):
            sumation += nums[end]
            if sumation >= target:
                flag= True
                while sumation - nums[begin] >= target and begin < end :
                    sumation -= nums[begin]
                    begin += 1

                length= (end - begin) + 1
                minLength= min(length, minLength)
            end += 1
        return minLength if flag else 0
