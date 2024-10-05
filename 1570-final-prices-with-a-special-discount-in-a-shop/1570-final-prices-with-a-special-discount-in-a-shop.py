class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        answer=[i for i in prices]
        for i  in  range(len(prices)):
            if stack == []:
                stack.append(i)
            else:
                while stack:
                    if prices[i] <= prices[stack[-1]]:
                        finalPrice= prices[stack[-1]] - prices[i]
                        answer[stack[-1]] = finalPrice
                        stack.pop()
                    else:
                        break
                stack.append(i)
        
        return answer