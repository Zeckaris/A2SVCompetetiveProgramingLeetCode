# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lst):
            rootPos= None
            if len(lst) % 2 != 0:
                rootPos= int((len(lst) + 1) / 2) - 1
            else:
                rootPos= int((len(lst)) // 2) 
            root= lst[rootPos]
            left= lst[: rootPos ]
            right= lst[rootPos + 1 :]
            node= TreeNode(root)
            if left:
                node.left= build(left)
            if right:
                node.right= build(right)
            return node
        head= build(nums)
                
        return head
        