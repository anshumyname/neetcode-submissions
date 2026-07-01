class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
            
        # STEP 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now at the end of the first half. 
        # 'slow.next' is the start of the second half.
        second = slow.next
        # We must sever the tie between the two halves!
        slow.next = None 
        
        # STEP 2: Reverse the second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # STEP 3: Merge the two halves
        # 'head' is the start of the first half
        # 'prev' is the start of the reversed second half
        first, second = head, prev
        while second:
            # Save the next nodes
            tmp1, tmp2 = first.next, second.next
            
            # Connect the nodes: first -> second -> tmp1
            first.next = second
            second.next = tmp1
            
            # Shift pointers forward for the next iteration
            first, second = tmp1, tmp2