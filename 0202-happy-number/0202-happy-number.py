from typing import List
class Solution:
    def isHappy(self, n: int) -> bool:
        def partition(n:int)->List[int]:
            summation=0
            while n >= 1:
                modulo= n % 10
                summation= summation + pow(modulo, 2)
                n= n // 10
            return summation

        slow, fast= n, partition(n)

        while slow != fast and fast != 1:
            slow= partition(slow)
            fast = partition(partition(fast))

            
        return fast==1