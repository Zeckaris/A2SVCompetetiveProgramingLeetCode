import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hsmap = {}
        for path in paths:
            separated = path.split(" ")
            directory = separated[0]
            
            for i in separated[1:]:
                filename, content = i.split("(")
                content = content[:-1] 
                full_path = f"{directory}/{filename}"

                if content not in hsmap:
                    hsmap[content] = []  
                hsmap[content].append(full_path) 
        result = [i for i in hsmap.values() if len(i) > 1]
        
        return result