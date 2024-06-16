def del_head(head):
    if head==None:
        return None
    elif head.next==head:
        return None
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=head.next
    return curr.next


def del_(head):
    if head==None:
        return None
    elif head.next==head:
        return None
    else:
        head.data=next.data
        head.next=head.next.next
        return head
    
# Deletion at Kth position 
def  delkth(head,k):
    if head==None:
        return None
    elif k==1:
        return del_head(head)
    else:
        for i in range(k-2):
            curr=curr.next
        curr.next=curr.next.next
        return head            

