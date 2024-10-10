class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hsmp= dict()
        verticeCount=0
        for i in edges:
            if i[0] not in hsmp:
                hsmp[i[0]]= 1
                verticeCount += 1
            else:
                hsmp[i[0]] += 1
            
            if i[1] not in hsmp:
                hsmp[i[1]]= 1
                verticeCount += 1
            else:
                hsmp[i[1]] += 1
        
        
        for key, value in hsmp.items():
            if value ==  verticeCount - 1:
                return key
        