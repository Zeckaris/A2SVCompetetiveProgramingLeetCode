from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize= len(s1)
        hsh= Counter(s1)
        temp= Counter(s2[:windowSize])
        if temp == hsh:
            return True
        for i in range(windowSize,len(s2) ):
            elementToBeRemoved= s2[i - windowSize]
            temp[elementToBeRemoved] -= 1
            temp[s2[i]] += 1
            if temp == hsh:
                return True
        return False

        