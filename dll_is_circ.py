class Solution: 
    def isCircular(self, head):
        if head==None:
            return 0
        curr=head.next
        while curr!=head and curr!=None:
            curr=curr.next
        if curr==head:
            return 1
        else:
            return 0
        