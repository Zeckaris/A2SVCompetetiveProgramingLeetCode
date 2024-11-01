class Solution:
    def makeFancyString(self, s: str) -> str:
        repeatation=[]
        i=0
        while i < len(s):
            if repeatation == []:
                repeatation.append(s[i])
                i += 1
            else:
                if s[i] in repeatation:
                    if len(repeatation) < 2:
                        repeatation.append(s[i])
                        i += 1
                    else:
                        new_string = s[:i] + s[i+1:]
                        s=new_string
                else:
                    repeatation=[s[i]]
                    i += 1
                    
        return s


        