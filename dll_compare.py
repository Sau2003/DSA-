class Solution:
    @staticmethod
    def compareCLL(head1, head2):
        # If both lists are empty, return True
        if head1 is None and head2 is None:
            return 1
    
        # If only one list is empty, return False
        if head1 is None or head2 is None:
            return 0
    
        # Traverse both lists simultaneously
        current1 = head1
        current2 = head2
    
        while True:
            # If data of current nodes is different, return False
            if current1.data != current2.data:
                return 0
    
            # Move to the next nodes
            current1 = current1.next
            current2 = current2.next
    
            # If one of the lists reaches the end, break the loop
            if current1 == head1 or current2 == head2:
                break
    
        # If both lists reach back to their heads, return True
        if current1 == head1 and current2 == head2:
            return 1
        else:
            return 0