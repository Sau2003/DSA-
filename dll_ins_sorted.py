def sortedInsert(head, x):
    new_node = Node(x)

    # If linked list is empty or x is smaller than the head, insert at the beginning
    if head is None or head.data >= x:
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

    current = head

    # Traverse the list to find the correct position to insert x
    while current.next is not None and current.next.data < x:
        current = current.next

    # Insert the new node after the current node
    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    new_node.prev = current

    return head