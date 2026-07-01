class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur:
            # 1. Save the next node so we don't lose the rest of the list
            temp = cur.next
            
            # 2. Reverse the actual pointer! (Point backwards)
            cur.next = prev
            
            # 3. Shift both pointers forward for the next iteration
            prev = cur
            cur = temp
            
        # At the end, 'cur' is None and 'prev' is the new head
        return prev