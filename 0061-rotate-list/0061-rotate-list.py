# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Don't do any operation if there is no node
        if not head:
            return head
        lastNode= head
        nodeCount= 1
        while lastNode.next:
            nodeCount += 1
            lastNode= lastNode.next 
        numOfRotations=  k % nodeCount
        #if the number of rotation is 0 return the same linked list
        if numOfRotations == 0:
            return head
            
        i=0
        new_last_node_pos= nodeCount - numOfRotations - 1
        new_last_node= head
        new_head= None
        while i < new_last_node_pos:
            new_last_node= new_last_node.next
            i += 1
        new_head= new_last_node.next
        lastNode.next= head
        new_last_node.next= None
        return new_head

        



        