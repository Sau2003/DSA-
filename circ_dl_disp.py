def displayList(head):
    result = []

    # If the list is empty, return empty list
    if not head:
        return result

    # Traverse the list forward to create the array
    current = head
    while True:
        result.append(str(current.data))
        current = current.next
        if current == head:
            break

    return result
