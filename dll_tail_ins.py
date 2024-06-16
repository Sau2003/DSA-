def insertInTail(head,data):
    temp=Node(data)
    if head==None:
        return temp 
    else:
        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=temp
        temp.prev=curr
        return head
            