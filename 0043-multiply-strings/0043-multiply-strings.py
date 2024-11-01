class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def getNum(num):
            for i in range(10):
                if f"{i}" == num:
                    print('returned ' ,i)
                    return i
                
        num1int =0
        for i in range(len(num1)):
            temp= getNum(num1[i])
            num1int = num1int * 10 + temp
       
        temp=0
        num2int=0
        for i in range(len(num2)):
            temp= getNum(num2[i])
            num2int = num2int * 10 + temp

        return f"{num1int * num2int}"




    

            
        