class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output= [0] * len(temperatures)
        i=0
        while i < len(temperatures):
            if len(stack) == 0:
                stack.append([temperatures[i], i])
            else:
                if stack[-1][0] <  temperatures[i]:
                    while stack[-1][0] < temperatures[i]:
                        diff= i - stack[-1][1]
                        output[stack[-1][1]]= diff
                        stack.pop()
                        if stack == []:
                            break
                    stack.append([temperatures[i],i])
                else:
                    stack.append([temperatures[i],i])
            i += 1
                        
        return output