class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
        
    def print_l(head):
        if head==None:
            return None
        print(head.key,end="")
        curr=head.next
        while curr!=head:
            curr=curr.next


# GFG 

def displayList(head):
    if head is None:
        return []

    result = []
    curr = head
    while True:
        result.append(curr.data)
        curr = curr.next
        if curr == head:
            break

    return result                            