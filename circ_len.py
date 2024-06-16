
def getLength(head):
    if head==None:
        return None
    c=1
    curr=head
    while curr.next!=head:
        curr=curr.next
        c+=1
    return c   