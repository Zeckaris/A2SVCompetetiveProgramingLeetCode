class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output= [0] * len(temperatures)
        i=0
        while i < len(temperatures):
            if stack != []:
                while stack[-1][0] < temperatures[i]:
                    output[stack[-1][1]]= i - stack[-1][1]
                    stack.pop()
                    if stack == []:
                        break
                stack.append([temperatures[i],i])
            else:
                stack.append([temperatures[i],i])
            i += 1
                        
        return output