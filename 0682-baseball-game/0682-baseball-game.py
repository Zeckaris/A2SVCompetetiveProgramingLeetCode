class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            try:
                num= int(i)
                stack.append(num)
            except:
                if stack:
                    if i == "C":
                        stack.pop()
                    elif i == "D":
                        temp= 2 * stack[-1]
                        stack.append(temp)
                    else:
                        temp= stack[-2] + stack[-1]
                        stack.append(temp)
            print(stack)    
        return sum(stack)


