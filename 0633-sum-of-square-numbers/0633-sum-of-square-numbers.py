class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt= int(c ** 0.5)
        begin=0
        end= sqrt
        while begin <= end:
            squareSum=  begin ** 2 + end ** 2
            if squareSum == c:
                return True
            elif squareSum < c:
                begin += 1
            elif squareSum > c:
                end -= 1
        return False
         

        