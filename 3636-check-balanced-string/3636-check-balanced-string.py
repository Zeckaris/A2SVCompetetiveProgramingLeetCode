class Solution:
    def isBalanced(self, num: str) -> bool:
        sumOdd=0
        sumEven=0
        for i in  range(len(num)):
            if i % 2 == 0:
                sumEven += int(num[i])
            else:
                sumOdd += int(num[i])
        return sumOdd == sumEven

        