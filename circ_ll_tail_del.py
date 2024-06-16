def deleteTail(head):
    if head is None or head.next == head:
        return None
    
    curr = head
    while curr.next.next != head:
        curr = curr.next
    
    curr.next = head
    return head