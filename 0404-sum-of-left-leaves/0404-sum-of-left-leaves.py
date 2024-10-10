# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftLeaves=[]
        left=[root.left]
        right=[root.right]
        
        while left or right:
            if left:
                rs= left.pop()
                if rs != None:
                    if rs.left == None and rs.right == None:
                        leftLeaves.append(rs.val)
                    else:
                        left.append(rs.left)
                        right.append(rs.right)
            if right:
                rs= right.pop()
                if rs != None:
                    left.append(rs.left)
                    right.append(rs.right)
                
        sum=0
        for i in leftLeaves:
            sum += i
        return sum
        