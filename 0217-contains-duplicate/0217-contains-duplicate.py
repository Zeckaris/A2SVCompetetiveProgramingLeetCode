class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev= None
        for i in nums:
            if prev == None:
                prev= i
            else:
                if prev == i:
                    return True
                else:
                    prev= i
        return False
        