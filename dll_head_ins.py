def insertInhead(head,data):
    temp=Node(data)
    if head!=None:
        head.prev=temp
    temp.next=head
    return temp
    #code here
