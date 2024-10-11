class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=0
        for i in range(len(s)):
            res ^= ord(s[i])
            res ^= ord(t[i])
        res ^= ord( t[-1])
        return chr(res)
        