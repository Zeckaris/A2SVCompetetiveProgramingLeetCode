from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []  
        line = "" 
        in_block_comment = False
        
        for i in range(len(source)):
            j = 0
            while j < len(source[i]):
                if in_block_comment:
                    if j + 1 < len(source[i]) and source[i][j] == '*' and source[i][j + 1] == '/':
                        in_block_comment = False  
                        j += 1 
                else:
                    if source[i][j] == '/' and j + 1 < len(source[i]):
                        if source[i][j + 1] == '/':
                            break
                        elif source[i][j + 1] == '*':
                            in_block_comment = True
                            j += 1  
                        else:
                            line += source[i][j]
                    else:
                        line += source[i][j]

                j += 1 
            
            if line and not in_block_comment:
                result.append(line)
                line = ""  
        
        return result
