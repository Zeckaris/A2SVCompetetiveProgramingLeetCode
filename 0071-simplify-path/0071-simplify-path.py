class Solution:
    def simplifyPath(self, path: str) -> str:
        #use a combination of stack and sliding window
        directories=path.split('/')
        stack=['/']
        for i in range(len(directories)):
            if directories[i] == '' or directories[i] == '.':
                continue
            elif directories[i] == '..':
                if len(stack) > 1:
                    stack.pop()
                while len(stack) > 1 and stack[-1] == '/':
                    stack.pop()
            else:
                if stack and stack[-1] != '/':
                    stack.append('/')
                stack.append(directories[i])

        return ''.join(stack)


            