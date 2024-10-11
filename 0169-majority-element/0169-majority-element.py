class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority= (len(nums) // 2)
        prev=nums[0]
        count=1
        for i in range(1,len(nums)):
            
            if  prev == nums[i]:
                count += 1
            else:
                count=1
                prev= nums[i]
            if count > majority:
                return prev
        return prev
    