class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        while i < len(word):
            if word[i] == ch:
                if i + 1 < len(word):
                    return word[i::-1] + word[i + 1:]
                else:
                    return  word[i::-1]
            i += 1
        return word
                


                

            
        