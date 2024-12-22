from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonChars= Counter(words[0])
        for i in range(1,len(words)):
            tempCount= Counter(words[i])
            commonChars &= tempCount
        
        result=[]
        for key , value in commonChars.items():
            for j in range(value):
                result.append(key)
        return result
        


        
       



        