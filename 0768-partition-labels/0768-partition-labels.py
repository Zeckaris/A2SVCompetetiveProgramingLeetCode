class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterDict= dict()
        for i in range(len(s)):
            if s[i] not in letterDict:
                letterDict[s[i]] = [i,-1]
            else:
                letterDict[s[i]][1]= i
        ans=[]
        begin=0
        end=-1
        start=0
        while begin < len(s):
            end= max(letterDict[s[begin]][1], end)
            if end == -1:
                ans.append(1)
                start= begin + 1
            else:
                if end ==  begin:
                    ans.append(end - start + 1)
                    start= end + 1
                    end= -1
            begin += 1
        return ans


    