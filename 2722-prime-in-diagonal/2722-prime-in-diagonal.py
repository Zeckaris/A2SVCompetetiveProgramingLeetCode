from math import sqrt
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        max_prime_num=0
        leftDiagonalR=0
        leftDiagonalC=0
        rightDiagonalR=0
        rightDiagonalC=len(nums) -1
        for i in range(len(nums)):
            if self.checkPrime(nums[leftDiagonalR][leftDiagonalC]):
                max_prime_num= max_prime_num if max_prime_num > nums[leftDiagonalR][leftDiagonalC] else nums[leftDiagonalR][leftDiagonalC]
            
            if self.checkPrime(nums[rightDiagonalR][rightDiagonalC]):
                max_prime_num= max_prime_num if max_prime_num > nums[rightDiagonalR][rightDiagonalC] else nums[rightDiagonalR][rightDiagonalC]
                
            leftDiagonalR += 1
            leftDiagonalC += 1
            rightDiagonalR += 1
            rightDiagonalC -= 1
        
        return max_prime_num
        
            
    def checkPrime(self,num:int)->bool:       
        sroot= int(sqrt(num))
        if num == 2:
            return True
        elif sroot < 2:
            return False
        for i in range (2,sroot + 1):
            if num % i == 0:
                return False
        return True