class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        s=s.strip()
        print(s)
        for i in s:
            if  i != " ":
                length += 1
            else:
                length=0
        return length
        