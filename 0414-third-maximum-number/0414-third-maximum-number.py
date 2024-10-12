class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxNums=[]
        for i in nums:
            if len(maxNums) < 3:
                if i not in maxNums:
                    maxNums.append(i)
            else:
                if i not in maxNums:
                    maxNums.sort()
                    if i > maxNums[0]:
                        maxNums[0]=i
        if len(maxNums) == 3:
            maxNums.sort()
            return maxNums[0]
        else:
            maxNums.sort()
            return maxNums[-1]