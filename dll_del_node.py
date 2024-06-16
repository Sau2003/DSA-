class Solution:
    def deleteNode(self, head, x):
        # If linked list is empty
        if head is None:
            return None

        # If position is 1, delete the head node
        if x == 1:
            temp = head
            head = temp.next
            if head:
                head.prev = None
            temp = None
            return head

        # Traverse to the position to be deleted
        current = head
        for _ in range(x - 1):
            if current is None:
                return head
            current = current.next

        # If position is out of range
        if current is None:
            return head

        # Delete the node at the given position
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        current = None

        return head
        # Code here