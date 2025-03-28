class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit():
                stack.append(s[i])
            else:
                if stack and stack[-1].isdigit():
                    stack.pop()
                else:
                    stack.append(s[i])
        return "".join(stack[::-1])

        