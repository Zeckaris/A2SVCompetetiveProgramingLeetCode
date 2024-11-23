from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k= len(p)
        startIndicies=[]
        chars=Counter(p)
        window= Counter(s[:k])
        if window == chars:
            startIndicies.append(0)

        for i in range(k, len(s)):
            if window[s[i - k]] <= 1:
                del window[s[i - k]]
            else:
                window[s[i - k]] -= 1
            
            window[s[i]] += 1
            if window == chars:
                startIndicies.append(i + 1 -k)
        
        return startIndicies

        