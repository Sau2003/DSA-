def displayList(head):
    result_forward = []

    # Forward traversal to create the array
    current = head
    while current:
        result_forward.append(current.data)
        current = current.next

    return result_forward
