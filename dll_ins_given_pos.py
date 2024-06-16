def addNode(head, p, x):
    new_node = Node(x)

    # If head is None or position is less than 0, insert at the beginning
    if head == None or p < 0:
        new_node.next = head
        if head != None:
            head.prev = new_node
        return new_node

    current = head
    count = 0

    # Traverse the list to find the position
    while current != None and count < p:
        current = current.next
        count += 1

    # If position is found, insert the new node after the current node
    if current != None:
        new_node.prev = current
        new_node.next = current.next
        if current.next != None:
            current.next.prev = new_node
        current.next = new_node

    return head