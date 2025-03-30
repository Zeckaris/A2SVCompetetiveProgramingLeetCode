class Solution:
    def longestPalindrome(self, s: str) -> str:
        #using dynamic programing
        longest=0
        longestString=s[0]
        dp= [[False] * len(s) for _ in range(len(s))]
        for  i in range(len(s)):
            for j in range(i + 1):
                if j == i:
                    dp[j][i]= True
                elif j + 1 == i:
                    if s[i] == s[j]:
                        dp[j][i]= True
                        if i - j + 1 > longest:
                            longest= i - j + 1
                            longestString= s[j: i + 1]
                    else:
                        dp[j][i]=False
                else:
                    if s[i] == s[j] and dp[j + 1][i-1] == True:
                        dp[j][i]= True
                        if i - j + 1 > longest:
                            longest= i - j + 1
                            longestString= s[j: i + 1]
                    else:
                        dp[j][i]=False
        
        return longestString
                    