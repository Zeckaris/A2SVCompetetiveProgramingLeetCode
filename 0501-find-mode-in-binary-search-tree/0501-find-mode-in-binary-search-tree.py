# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hsmp = dict() 
        stack = [root]
        max_freq = 0  
        modes = []     
        while stack:
            temp = stack.pop()
            if temp:
                hsmp[temp.val] = hsmp.get(temp.val, 0) + 1
                
                if hsmp[temp.val] > max_freq:
                    max_freq = hsmp[temp.val]
                    modes = [temp.val]  
                elif hsmp[temp.val] == max_freq:
                    modes.append(temp.val)  
                stack.append(temp.right)
                stack.append(temp.left)

        return modes
        