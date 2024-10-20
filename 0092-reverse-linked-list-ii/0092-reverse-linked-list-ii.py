# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node,n):
            if n == 1:
                return node , node.next
            firstNode, lastNode = reverse(node.next, n - 1)
            node.next.next= node
            node.next=lastNode
            return firstNode,lastNode
        
        if left == 1:
            newNode, lastLink= reverse(head,right)
            return newNode
        
        head.next= self.reverseBetween(head.next,left -1 ,right - 1)
        return head







            
            

            
           


        


