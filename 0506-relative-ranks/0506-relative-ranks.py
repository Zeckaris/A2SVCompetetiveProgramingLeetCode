class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        unsorted= [i for i in score]
        score.sort(reverse=True)
        hsmp={value:i for i,value in enumerate(score)}
        result=[]
        for i in unsorted:
            if hsmp[i] == 0:
                result.append("Gold Medal")
            elif hsmp[i] == 1:
                result.append("Silver Medal")
            elif hsmp[i] == 2:
                result.append("Bronze Medal")
            else:
                result.append(f'{hsmp[i] + 1}')
        return result
        
     
        