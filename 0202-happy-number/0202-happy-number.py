from typing import List
class Solution:
    def isHappy(self, n: int) -> bool:
        def partition(n:int)->List[int]:
            lst=[]
            while n >= 1:
                modulo= n % 10
                n= n // 10
                lst.append(modulo)
            summation= 0
            for i in lst:
                summation += pow(i,2)
            return summation
        cycleDetect= set()
        check= n
        while True:
            check= partition(check)
            if check == 1:
                return True
            elif check in cycleDetect:
                return False
            cycleDetect.add(check)
        return False


        

        