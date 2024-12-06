class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cumulative=[0] * (len(s) + 1)
        for i in range(len(shifts)):
            cumulative[shifts[i][0]] +=1 if shifts[i][2] == 1 else - 1
            if shifts[i][1] + 1 < len(cumulative):
                cumulative[shifts[i][1] + 1] += -1 if shifts[i][2] == 1 else 1

        for i in range(1, len(cumulative)):
            cumulative[i] += cumulative[i - 1]

        newString=list(s)
        for i in range(len(s)):
            shift= cumulative[i]
            afterShift= chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            newString[i]= afterShift

        return ''.join(newString)

        