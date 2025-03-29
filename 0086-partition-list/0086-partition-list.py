class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head =ListNode(0)
        small_tail = small_head  
        large_head =ListNode(0)
        large_tail = large_head  

        temp = head
        while temp:
            if temp.val < x:
                small_tail.next = temp 
                small_tail = temp
            else:
                large_tail.next = temp  
                large_tail = temp

            temp = temp.next 

        large_tail.next = None  
        small_tail.next = large_head.next 

        return small_head.next 
