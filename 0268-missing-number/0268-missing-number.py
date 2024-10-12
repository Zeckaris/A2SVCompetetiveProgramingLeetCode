class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        status=0
        multiplication=1
        total = sum(range(0, len(nums) + 1))
        for i in range(len(nums)):
            status += nums[i]
            multiplication *= nums[i]
        if multiplication != 0:
            return 0
        return total - status
        

        