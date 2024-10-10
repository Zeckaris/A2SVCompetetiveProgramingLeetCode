class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        hashmp=dict()
        visited= set()
        for key , value  in edges:
            if key in hashmp:
                hashmp[key].append(value)
            else:
                hashmp[key] =[value] 
                
            if value in hashmp:
                hashmp[value].append(key)
            else:
                hashmp[value] = [key]    
       
        stack=[source]
        while stack:
            traversePoint= stack.pop() 
            if traversePoint in hashmp and traversePoint not in visited:
                visited.add(traversePoint)
                for i in hashmp[traversePoint]:
                    if i == destination:
                        return True
                    else:
                        stack.append(i)
        
        return False