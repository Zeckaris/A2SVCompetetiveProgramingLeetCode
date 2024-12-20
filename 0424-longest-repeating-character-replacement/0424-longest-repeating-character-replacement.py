class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #dynamic sliding window
        maxFreq= 0
        freq= dict()
        begin= 0
        longestWindow= 0
        for end in range(len(s)):
            freq[s[end]]= freq.get(s[end],0) + 1
            maxFreq= max(maxFreq, freq[s[end]])

            if (end - begin + 1) - maxFreq > k:
                freq[s[begin]] -= 1
                begin += 1

            longestWindow= max(longestWindow,(end - begin + 1))
        return longestWindow
            

            


        
