class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS=[]
        stackT=[]
        for i in s:
            if i != '#':
                stackS.append(i)
            else:
                if stackS:
                    stackS.pop()
        
        for i in t:
            if i != '#':
                stackT.append(i)
            else:
                if stackT:
                    stackT.pop()
        
        if stackS == stackT:
            return True
        else:
            return False
            

        