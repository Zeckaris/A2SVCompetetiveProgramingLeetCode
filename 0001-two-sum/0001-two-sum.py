class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic= {key:value for value , key in enumerate(nums)}
        for i in range(len(nums)):
            complement= target - nums[i]
            if complement in dic and dic[complement] != i:
                return [dic[complement],i]
        return []

        