# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        temp= head
        prev= None
        prePrev=None
       
        while  temp:
            if count % 2 != 0:
                prePrev = prev
                prev= temp
                temp= temp.next
            else:
                tmp = temp.next
                if prePrev:
                    prePrev.next = temp 
                else:
                    head = temp 

                temp.next = prev 
                prev.next = tmp 
                prePrev = prev
                temp = prev.next    
            
            count += 1         
             
        return head




        
        
        