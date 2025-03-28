class Solution:
    def countSubstrings(self, s: str) -> int:
        matx=[[False]*len(s) for _ in range(len(s))]
        count= 0
        for i in range(len(s)):
            for j in range(i + 1):
                if  i == j:
                    matx[j][i]= True
                elif i == j + 1:
                    matx[j][i]= s[i] == s[j]
                else:
                    matx[j][i]= (s[i] == s[j] and matx[j + 1][i - 1])
                count += 1 if matx[j][i] else 0
        return count
        