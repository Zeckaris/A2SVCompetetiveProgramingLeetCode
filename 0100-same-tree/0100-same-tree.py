# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p == None and q == None:
        #     return True
        # elif p== None and q != None  or p != None and q == None:
        #     return False

        # stack1=[]
        # stack2=[]
        # if p != None:
        #     stack1.append(p)
        # if q != None:
        #     stack2.append(q)
        # while stack1  and stack2 :
        #     tmp1= stack1.pop()
        #     tmp2= stack2.pop()
        #     if tmp1.val != tmp2.val:
        #         return False

        #     if tmp1.right  and tmp2.right:
        #         stack1.append(tmp1.right)
        #         stack2.append(tmp2.right)
        #     elif tmp1.right or tmp2.right:
        #         return False
                
        #     if tmp1.left  and tmp2.left :
        #         stack1.append(tmp1.left)
        #         stack2.append(tmp2.left)
        #     elif tmp1.left or tmp2.left:
        #         return False
            
        # return True
        queue1=deque([p])
        queue2=deque([q])
        
        while  queue1 and queue2:
            temp1= queue1.popleft()
            temp2= queue2.popleft()
            if temp1  and temp2:
                if temp1.val != temp2.val:
                    return False
                else:
                    queue1.append(temp1.left)
                    queue2.append(temp2.left)
                
                    queue1.append(temp1.right)
                    queue2.append(temp2.right)
            elif (temp1 == None and temp2 != None) or  (temp1 != None and temp2 == None):
                return False
                
        return True
        
                


        