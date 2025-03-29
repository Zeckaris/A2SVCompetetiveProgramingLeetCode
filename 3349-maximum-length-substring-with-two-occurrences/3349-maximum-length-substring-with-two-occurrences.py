class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        stringDict = {}
        begin = 0
        maxSize = 0

        for end in range(len(s)):  
            stringDict[s[end]] = stringDict.get(s[end], 0) + 1

            while stringDict[s[end]] > 2:
                stringDict[s[begin]] -= 1
                begin += 1

            maxSize = max(maxSize, end - begin + 1)

        return maxSize
            
                

                            

        