class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        orderSet=False
        order=''
        for i in range(1,len(nums)):
            if orderSet == False and nums[i] != nums[i - 1]:
                if nums[i - 1] < nums[i]:
                    order='i'
                else:
                    order= 'd'
                
                orderSet=True
            elif order == 'i':
                if nums[i] < nums[i - 1]:
                    return False
            elif order == 'd':
                if nums[i] > nums[i - 1]:
                    return False
        return True