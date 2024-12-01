class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterDict= dict()
        for i in range(len(s)):
            letterDict[s[i]] = i

        ans=[]
        begin=0
        end=0
        start=0
        while begin < len(s):
            end= max(letterDict[s[begin]], end)
            if end ==  begin:
                ans.append(end - start + 1)
                start= end + 1
                end= 0

            begin += 1

        return ans


    