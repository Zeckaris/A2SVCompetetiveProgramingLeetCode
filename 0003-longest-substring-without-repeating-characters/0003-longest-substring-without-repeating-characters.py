class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        uniqueCharactersSet= set()
        windowInitial=0
        for index,val in enumerate(s):
            if val in uniqueCharactersSet:
                for i in range(windowInitial, index):
                    if s[i] != val:
                        uniqueCharactersSet.discard(s[i])
                    else:
                        windowInitial= i + 1
                        break
                maxLength= max(maxLength, len(uniqueCharactersSet))
                
            else:
                uniqueCharactersSet.add(val)
                maxLength= max(maxLength, len(uniqueCharactersSet))
            
        return maxLength


        