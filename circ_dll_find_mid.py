class Solution:
    def findMiddle(self, head):
        if head is None:
            return None

        slow_ptr = head
        fast_ptr = head

        # Move fast pointer two steps and slow pointer one step at a time
        while fast_ptr.next != head and fast_ptr.next.next != head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # If the list has odd number of elements, return the data of slow pointer
        # If the list has even number of elements, return the data of slow pointer's next node
        return slow_ptr.data if fast_ptr.next == head else slow_ptr.next.data