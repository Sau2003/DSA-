# Insertion at the begin
def insert(head,x):
    temp=Node(x)
    if head==None:
        temp.next=temp
        return temp
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return temp

def insert(head,x):
    temp=Node(x)
    if head==None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next
        head.next=temp
        head.key,temp.key=temp.key,head.key
        return head
    
# Insertion at the end 
def insert_end(head,x):
    temp=Node(x)
    if head==None:
        temp.next=temp
        return temp
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return head

def insert(head,x):
    temp=Node(x)
    if head==None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next
        head.next=temp
        temp.data,head.data=head.data,temp.data
        return temp
            